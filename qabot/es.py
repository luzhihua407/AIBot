import json

from elasticsearch import Elasticsearch

index_name = "qa_set"
mapping = {
    "properties": {
        "question": {
            "type": "text",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_smart"
        }
    }
}

es = Elasticsearch()


def createIndex(index, data_set):
    """
    :param index:
    :param data_set json for data list

    """
    # es.indices.delete(index=index, ignore=[400, 404])
    # print("%s index deleted" % index)
    es.indices.create(index=index, ignore=[400, 404])
    es.indices.put_mapping(index=index, doc_type='qa', body=mapping, include_type_name=True)
    # for doc in data_set:
    for idx, doc in enumerate(data_set):
        # print(doc)
        es.index(index=index, id=idx, body=doc)
    print("%s index finished" % index)


def createIndex(index, doc_id, doc):
    """
    :param index:
    :param data_set json for data list

    """
    # es.indices.delete(index=index, ignore=[400, 404])
    # print("%s index deleted" % index)
    es.indices.create(index=index, ignore=[400, 404])
    es.indices.put_mapping(index=index, doc_type='qa', body=mapping, include_type_name=True)
    es.index(index=index, id=doc_id, body=doc)
    print("%s %d index finished" % (index, doc_id))


def search(index, text, size):
    """
    :param index:
    :param text: text to search
    :return: hits result
    """
    dql = {
        "from": 0,
        "size": size,  # 返回十条数据
        'query': {
            'match': {
                'question': text
            }
        }
    }
    res = es.search(index=index, body=dql)
    questions = []
    answers = []
    for hit in res['hits']['hits']:
        _source = json.dumps(hit["_source"])
        questions.append(hit["_source"]["question"])
        answers.append(hit["_source"]["answer"])
        print(hit["_score"], hit["_source"])
    return questions, answers


def search_similar(index, text, size):
    """
    :param index:
    :param text: text to search
    :return: hits result
    """
    dql = {
        "from": 0,
        "size": size,  # 返回十条数据
        'query': {
            'match': {
                'sq': text
            }
        }
    }
    res = es.search(index=index, body=dql)
    questions = []
    answers = []
    for hit in res['hits']['hits']:
        _source = json.dumps(hit["_source"])
        questions.append(hit["_source"]["question"])
        answers.append(hit["_source"]["answer"])
        print(hit["_score"])
        print(hit["_source"])
    return questions, answers


def search_random(index, size=5):
    """
    随机取条数
    :param index: 索引
    :param size: 条数
    :return:
    """
    dql = {
        "from": 0,
        "size": size,  # 返回十条数据
        "query": {
            "bool": {
                "filter": [
                    {"term": {"valid": True}},
                ]
            }
        },
        "sort": {  # 排序
            "_script": {  # key原封不动
                "type": "number",
                "script": "Math.random()",  # 随机排序
                "order": "asc"
            }
        }
    }
    res = es.search(index=index, body=dql)
    print("Got %d Hits:" % res['hits']['total']['value'])
    questions = []
    answers = []
    for hit in res['hits']['hits']:
        _source = json.dumps(hit["_source"])
        questions.append(hit["_source"]["question"])
        answers.append(hit["_source"]["answer"])
        print(hit["_source"])
    return questions, answers
