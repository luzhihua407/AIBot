""" 利用倒排表进行优化 """


class InvertTable:

    def __init__(self, qList_kw):
        invertTable = {}
        for idx, tmpLst in enumerate(qList_kw):
            for kw in tmpLst:
                if kw in invertTable.keys():
                    invertTable[kw].append(idx)
                else:
                    invertTable[kw] = [idx]
        self.invertTable = invertTable

    def filterData(self,inputQuestionKW,questionList,answerList):
        idxLst = []
        questions = []
        answers = []
        for kw in inputQuestionKW:
            if kw in self.invertTable.keys():
                idxLst.extend(self.invertTable[kw])
        idxSet = set(idxLst)
        for idx in idxSet:
            questions.append(questionList[idx])
            answers.append(answerList[idx])
        return questions, answers

    def invert_idxTable(qList_kw):  # 定一个一个简单的倒排表
        invertTable = {}
        for idx, tmpLst in enumerate(qList_kw):
            for kw in tmpLst:
                if kw in invertTable.keys():
                    invertTable[kw].append(idx)
                else:
                    invertTable[kw] = [idx]
        return invertTable


    def filter_questionByInvertTab(inputQuestionKW, questionList, answerList, invertTable):
        idxLst = []
        questions = []
        answers = []
        for kw in inputQuestionKW:
            print(kw)
            print("--------")
            print(invertTable.keys())
            print("--------")
            if kw in invertTable.keys():
                idxLst.extend(invertTable[kw])
        idxSet = set(idxLst)
        for idx in idxSet:
            questions.append(questionList[idx])
            answers.append(answerList[idx])
        return questions, answers
