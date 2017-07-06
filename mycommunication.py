import urllib.request
import ast

def inputUrlreturnDict(url):
    req = urllib.request.Request(url)

    try:
        dict = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        return e

    dict = dict.decode(encoding='UTF-8')
    dict = urllib.request.unquote(dict)
    dict = ast.literal_eval(dict)

    return dict