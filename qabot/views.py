import json
import random
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from flask import jsonify

from chatbot.views import chat_bot
from qabot import CollectQuery, es
from qabot.ResponseMessage import ResponseMessage
from qabot.jiebaSegment import Seg
from qabot.models import FQA
from qabot.sentenceSimilarity import SentenceSimilarity
from django.apps import AppConfig


def invert_idxTable(qList_kw):  # 定一个一个简单的倒排表
    invertTable = {}
    for idx, tmpLst in enumerate(qList_kw):
        for kw in tmpLst:
            if kw in invertTable.keys():
                invertTable[kw].append(idx)
            else:
                invertTable[kw] = [idx]
    return invertTable


def filter_questionByInvertTab(inputQuestionKW):
    invertTable = invert_idxTable(AppConfig.qList_kw)
    idxLst = []
    questions = []
    answers = []
    for kw in inputQuestionKW:
        if kw in invertTable.keys():
            idxLst.extend(invertTable[kw])
    idxSet = set(idxLst)
    for idx in idxSet:
        questions.append(AppConfig.questionList[idx])
        answers.append(AppConfig.answerList[idx])
    return questions, answers


def query(q):
    seg = Seg()
    # 搜索问题
    questionList_s, answerList_s = es.search(es.index_name, q, 3)
    # 搜索类似问题
    questionList_sq, answerList_sq = es.search_similar(es.index_name, q, 3)
    if len(questionList_sq) > 0 and len(answerList_sq) > 0:
        # 合并list
        questionList_s.extend(questionList_sq)
        answerList_s.extend(answerList_sq)
        # 去重
        questionList_s = list(set(questionList_s))
        answerList_s = list(set(answerList_s))
    if len(questionList_s) >= 1:
        tips = "你是不是想问："
        questionList = questionList_s
        answerList = answerList_s
    else:
        questionList, answerList = es.search_random(es.index_name, 5)
        tips = "不好意思，我还学习中，点击以下问题试试："
        CollectQuery.collect(q)
    # # 初始化模型
    ss = SentenceSimilarity(seg)
    time1 = time.time()
    ss.set_sentences(questionList)
    time2 = time.time()
    print("time2 {}".format(time2 - time1))
    # ss.TfidfModel()  # tfidf模型
    # ss.LdaModel()
    ss.LsiModel()
    time3 = time.time()
    print("time3 {}".format(time3 - time2))
    time1 = time.time()
    question_k = ss.similarity_k(q, 3)
    length = len(question_k)
    questions = []
    for idx, score in zip(*question_k):
        questions.append(questionList[idx])
        print(
            "same questions： {}   answer: {}               score： {}".format(questionList[idx], answerList[idx], score))
    for idx, score in zip(*question_k):
        if score >= 1:
            return ResponseMessage(None, answerList[question_k[0][0]], None)

        else:
            question = questionList[question_k[0][0]]
            if question == q:
                return ResponseMessage(None, answerList[question_k[0][0]], None)
            elif question != q and 0.9 < score < 1:
                return ResponseMessage(None, answerList[question_k[0][0]], None)
            else:
                return ResponseMessage(tips, None, questions)


def tall(request):
    q = request.GET.get("q")

    data = chat_bot(q)

    if data == "Sorry, I don't have an answer for that!":
        resp = query(q)
    else:
        resp = ResponseMessage(None, data, None)
    data = json.dumps(resp.__dict__, ensure_ascii=False)  # convert to json
    rs = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return rs


def index(request):
    context = {}
    return render(request, 'qabot/index.html', context)
