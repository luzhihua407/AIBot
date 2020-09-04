from django.shortcuts import render

from qabot.apps import initData
from qabot.models import FQA


def load(request):
    context = {"msg": "热更新完成"}
    data = FQA.objects.exclude(valid=True).exclude(answer__isnull=True).exclude(answer__exact='')
    initData(data)
    for o in data:
        FQA.objects.filter(question=o).update(valid=True)
        print("update %s" % o)
    return render(request, 'qabot/loadData.html', context)





