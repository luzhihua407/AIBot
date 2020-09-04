import gensim
from django.test import TestCase

# Create your tests here.
from datetime import datetime
from elasticsearch import Elasticsearch
from gensim.models import CoherenceModel
#
# mapping = {
#     "properties": {
#         "question": {
#             "type": "text",
#             "analyzer": "ik_max_word",
#             "search_analyzer": "ik_smart"
#         }
#     }
# }
#
#
# def set_mapping(es, index_name="test-index", doc_type_name=None):
#     mapping = {
#         "properties": {
#             "question": {
#                 "type": "text",
#                 "analyzer": "ik_smart",
#                 "search_analyzer": "ik_smart"
#             }
#         }
#     }
#     es.indices.put_mapping(index=index_name, doc_type=doc_type_name, body=mapping)
#
#
# es = Elasticsearch()
#
# doc = {
#     'question': '怎样提高绘制电子围栏的精准度',
#     'answer': '<p>1. 按住并拖拽线条，可调整围栏，建议沿河流、道路等显著地标划分边界，分界线尽量避开货主密集区域，切勿留下盲区，以免定位偏移导致订单被分配到其他门店或者无法判断订单归属门店。</p> <p>2. '
#               '点击左上角按钮可切换到卫星地图模式，辅助精确识别位置；</p> <p>3. 门店紧密交界的地方线条可以重叠，但是不要留下空白。</p>',
# }
# es.indices.delete(index="test-index", ignore=[400, 404])
# res = es.indices.create(index="test-index", ignore=[400, 404])
# es.indices.put_mapping(index='test-index', doc_type='politics', body=mapping, include_type_name=True)
# res = es.index(index="test-index", id=1, body=doc)
# # set_mapping(es, None, None)
# print(res['result'])
# res = es.get(index="test-index", id=1)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")
# # 全文检索
# dql = {
#     'query': {
#         'match': {
#             'question': '提高'
#         }
#     }
# }
# res = es.search(index='test-index', doc_type='politics', body=dql)
# # res = es.search(index="test-index", body={"query": {"match_all": {}}})
# body={
#     "text": "美国阿拉斯加州发生8.0级地震",
#     "tokenizer": "ik_max_word"
# }
# a = es.indices.analyze(body=body, index="test-index")
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print(hit["_source"])
import nltk
nltk.download()
