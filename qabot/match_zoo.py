from pprint import pprint

import matchzoo as mz
from sklearn import preprocessing  # 用于正则化
train_pack = mz.datasets.wiki_qa.load_data('train', task='ranking')
valid_pack = mz.datasets.wiki_qa.load_data('dev', task='ranking')
pprint(train_pack)
pprint(valid_pack)
preprocessor = mz.preprocessors.DSSMPreprocessor()
train_processed = preprocessor.fit_transform(train_pack)
valid_processed = preprocessor.transform(valid_pack)
ranking_task = mz.tasks.Ranking(loss=mz.losses.RankCrossEntropyLoss(num_neg=4))
ranking_task.metrics = [
    mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
    mz.metrics.MeanAveragePrecision()
]
model = mz.models.DSSM()
model.params['input_shapes'] = preprocessor.context['input_shapes']
model.params['task'] = ranking_task
model.guess_and_fill_missing_params()
model.build()
model.compile()

train_generator = mz.PairDataGenerator(train_processed, num_dup=1, num_neg=4, batch_size=64, shuffle=True)
valid_x, valid_y = valid_processed.unpack()
evaluate = mz.callbacks.EvaluateAllMetrics(model, x=valid_x, y=valid_y, batch_size=len(valid_x))
history = model.fit_generator(train_generator, epochs=1, callbacks=[evaluate], workers=5, use_multiprocessing=True)
y_pred=model.predict(valid_x)
print(y_pred)
# left_id = valid_x['id_left']
# right_id = valid_x['id_right']
# assert (len(left_id) == len(left_id))
# assert (len(left_id) == len(y_pred))
# assert (len(valid_y) == len(y_pred))
Scale = preprocessing.MinMaxScaler(feature_range=(0, 1))  # 对结果做规范化
y_pred = Scale.fit_transform(y_pred)
