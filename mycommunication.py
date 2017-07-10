import urllib.request
import ast
import json

def inputUrlreturnDict(url):
    req = urllib.request.Request(url)

    try:
        dict = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    dict = dict.decode(encoding='UTF-8')
    dict = urllib.request.unquote(dict)

    dict = json.loads(dict)

    return dict

def getChampionInfo(id, apiKey):
    list = []
    url = "https://kr.api.riotgames.com/lol/static-data/v3/champions/{}?locale=ko_KR&tags=all&api_key={}".format(id, apiKey)

    req = urllib.request.Request(url)

    try:
        info = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    info = info.decode(encoding='UTF-8')
    info = json.loads(info)

    list.append(info['name'])
    list.append(info['tags'])

    return list

def tierDict(url):
    req = urllib.request.Request(url)

    try:
        dict = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    dict = dict.decode(encoding='UTF-8')

    if dict == '[]':
        return 'unranked'

    dict = dict[1:-1]
    dict = urllib.request.unquote(dict)

    dict = dict.replace("true", "'true'")
    dict = dict.replace("false", "'false'")
    dict = ast.literal_eval(dict)

    if(type(dict) is tuple):
        dict = dict[0]
    else:
        pass


    return dict

def recnetDict(url):
    req = urllib.request.Request(url)

    try:
        dict = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    dict = dict.decode(encoding='UTF-8')
    dict = urllib.request.unquote(dict)

    dict = json.loads(dict)

    return dict


if __name__ == '__main__':
    print(getChampionInfo(114, "RGAPI-0f10c455-7071-46ec-9e93-0d1a688198bc"))