import json

from django.apps import AppConfig

from qabot import es


class QABotConfig(AppConfig):
    name = 'qabot'

    def ready(self):
        fqa = self.get_model('fqa', True)
        data = fqa.objects.filter(valid=1)
        initData(data)


def initData(data):
    for o in data:
        kw = {}
        sq = o.sq.all()
        for q in sq:
            kw.setdefault("sq", q.question)
        kw.setdefault("question", o.question)
        kw.setdefault("answer", o.answer)
        kw.setdefault("valid", o.valid)
        es.createIndex(es.index_name, o.id, kw)
