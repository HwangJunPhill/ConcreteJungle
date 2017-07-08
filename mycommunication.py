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

def getChampionName(id):
    url = "https://global.api.riotgames.com/api/lol/static-data/KR/v1.2/champion/{}?api_key=RGAPI-37384fa5-73b5-45ac-aeca-2c72560b52d3".format(id)

    req = urllib.request.Request(url)

    try:
        info = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    info = info.decode(encoding='UTF-8')
    info = urllib.request.unquote(info)
    info = json.loads(info)

    return info['name']

def tierDict(url):
    req = urllib.request.Request(url)

    try:
        dict = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    dict = dict.decode(encoding='UTF-8')
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