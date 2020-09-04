import typing
from pathlib import Path

from pathlib import Path

import matchzoo as mz
import pandas as pd

import qabot.chinese_tokenize as ct


def read_data(path):
    table = pd.read_csv(path)
    df = pd.DataFrame({
        'text_left': table['sentence1'],
        'text_right': table['sentence2'],
        'label': table['label']
    })
    return mz.pack(df)


def load_data(
        stage: str = 'train',
        filtered: bool = False,
        return_classes: bool = False
) -> typing.Union[mz.DataPack, tuple]:
    if stage not in ('train', 'dev', 'test'):
        raise ValueError(f"{stage} is not a valid stage."
                         f"Must be one of `train`, `dev`, and `test`.")

    data_root = Path("C:\\Users\\86137\\Desktop")
    file_path = data_root.joinpath(f'{stage}.csv')
    data_pack = read_data(file_path)
    return data_pack


train_raw = load_data(stage='train')
ranking_task = mz.tasks.Ranking(loss=mz.losses.RankCrossEntropyLoss(num_neg=0))
ranking_task.metrics = [
    mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
    mz.metrics.MeanAveragePrecision()
]
preprocessor_class = mz.preprocessors.BasicPreprocessor()
preprocessor_class._units = [
    ct.ChineseTokenize(),
    mz.preprocessors.units.punc_removal.PuncRemoval(),
]

model_class = mz.models.MVLSTM
model, preprocessor, data_generator_builder, embedding_matrix = mz.auto.prepare(
    task=ranking_task,
    model_class=model_class,
    preprocessor=preprocessor_class,
    data_pack=train_raw
)

train_processed = preprocessor.fit_transform(train_raw, verbose=1)
tuner = mz.auto.Tuner(
    params=model.params,
    train_data=train_processed,
    test_data=train_processed,
    num_runs=10
)
results = tuner.tune()
print(results['best'])
params = results['best']['sample']
print(params)
model.params['input_shapes'] = preprocessor.context['input_shapes']
model.params['mlp_num_fan_out'] = params['mlp_num_fan_out']
model.params['mlp_num_layers'] = params['mlp_num_layers']
model.params['mlp_num_units'] = params['mlp_num_units']
model.params['top_k'] = params['top_k']
model.compile()
model.build()
model.save('my-model')
loaded_model = mz.load_model('./my-model')
print("after==================================")
print(loaded_model.params)  # 展示模型中可调参数
