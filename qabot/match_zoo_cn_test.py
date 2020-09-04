import typing
from pathlib import Path

import matchzoo as mz
import numpy as np
import pandas as pd
from sklearn import preprocessing  # 用于正则化
import qabot.chinese_tokenize as ct


def read_data(path):
    table = pd.read_csv(path)
    df = pd.DataFrame({
        'text_left': '怎样提高绘制电子围栏的精准度',
        'text_right': table['sentence1'],
        # 'label': table['label']
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


test_raw = load_data(stage='test')
# preprocessor_class = mz.preprocessors.BasicPreprocessor()
# preprocessor_class._units = [
#     # ct.ChineseTokenize(),
#     mz.preprocessors.units.punc_removal.PuncRemoval(),
# ]
loaded_model = mz.load_model('./my-model')
# fit_test_raw = loaded_model.fit(test_raw)
test_pack_processed = loaded_model.fit_transform(test_raw)
test_x, test_y = test_pack_processed.unpack()
# eva = loaded_model.evaluate(test_x, test_y)
print(test_raw.right)
# print(fit_test_raw.context['vocab_unit'].state['index_term'])
arr = loaded_model.predict(test_x)
test_xgb = np.array(arr)
test_xgb = pd.DataFrame(test_xgb)
Scale = preprocessing.MinMaxScaler(feature_range=(0, 1))  # 对结果做规范化
y_pred = Scale.fit_transform(arr)
print(pd.DataFrame(arr))
vocab_unit = preprocessor_class.context['vocab_unit']  # 此部分是为了显示处理过程
for idx, sequence in enumerate(test_x['text_left']):
    print('left :%s %s' % (idx, sequence),
          '/'.join([vocab_unit.state['index_term'][i] for i in sequence]))
print("----------------------")
for idx, sequence in enumerate(test_x['text_right']):
    print('right :%s %s' % (idx, sequence),
          '/'.join([vocab_unit.state['index_term'][i] for i in sequence]))
