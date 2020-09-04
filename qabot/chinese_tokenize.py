import codecs

import jieba
from matchzoo.preprocessors.units.unit import Unit


def read_stop_word(self):
    file_obj = codecs.open(self.stop_word_filepath, 'r', 'utf-8')
    while True:
        line = file_obj.readline()
        line = line.strip('\r\n')
        if not line:
            break
        self.stopwords.add(line)
    file_obj.close()


def cut(self, sentence, stop_word=True, cut_all=False):
    seg_list = jieba.cut(sentence, cut_all)
    results = []
    for seg in seg_list:
        # if stop_word and seg in self.stopwords:
        #     continue
        results.append(seg)

    return results





class ChineseTokenize(Unit):
    """Process unit for text containing Chinese tokens."""
    stop_word_filepath = "./stopwordList/stopword.txt"
    user_dict_filepath = './userdict/userdict.txt'

    def __init__(self):
        self.stopwords = set()
        jieba.load_userdict(self.user_dict_filepath)
        # read_stop_word(self)

    def transform(self, input_: str) -> str:
        """
        Process input data from raw terms to processed text.

        :param input_: raw textual input.

        :return output: text with at least one blank between adjacent
                        Chinese tokens.
        """
        # output = []
        #
        if isinstance(input_, float):
            return ""
        # for char in input_:
        #     cp = ord(char)
        #     if is_chinese_char(cp):
        #         output.append(" ")
        #         output.append(char)
        #         output.append(" ")
        #     else:
        #         output.append(char)
        seg_list = cut(self=self, sentence=input_, stop_word=False)
        return seg_list
        # return "".join(output)
