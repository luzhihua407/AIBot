from qabot.models import FQA


def collect(query):
    rs = FQA.objects.filter(question=query)
    if len(rs) == 0:
        FQA.objects.create(question=query, valid=False)


class CollectQuery:
    pass
