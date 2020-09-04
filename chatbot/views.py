import json
import os

import requests
from django.http import JsonResponse
# Create your views here.
from programy.clients.embed.configfile import EmbeddedConfigFileBot


def api(request):
    question = request.GET['question']
    url = 'http://127.0.0.1:8080/wxIntelligentInquiry/checkDiscount.action'
    params = {'no': question}
    response = requests.get(url=url, params=params)
    _json = json.loads(response.text)
    _data = _json['data']
    string_list = []
    for a, item in enumerate(_data):
        print(a)
        print(item['checkItem'])
        string_list.append('<li>'+item['checkItem']+'</li>')
    print("".join(string_list)+"-------")
    return JsonResponse("".join(string_list), safe=False, json_dumps_params={'ensure_ascii': False})


def chat_bot(q):
    config_file = "chatbot/config/windows/config.yaml"
    config_file = os.path.abspath(config_file)
    my_bot = EmbeddedConfigFileBot(config_file)
    client_context = my_bot.create_client_context("testuser")
    response = my_bot.process_question(client_context, q)
    return response
