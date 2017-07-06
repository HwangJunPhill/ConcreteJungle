import urllib.parse
import ast
from urllib import request, parse

class Summoner:
    def __init__(self, name):
        self.name = name

        if(type(self.name) is str):
            print("Summoner")
            self.getSummonerInfo()
        else:
            return

    def getSummonerInfo(self):
        print(self.name)

        url = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/{}?api_key=RGAPI-37384fa5-73b5-45ac-aeca-2c72560b52d3".format(urllib.request.quote(self.name))

        req = urllib.request.Request(url)

        data = urllib.request.urlopen(req).read()
        data = data.decode(encoding='UTF-8')
        data = urllib.request.unquote(data)
        data = ast.literal_eval(data)

        print(data[self.name])


if __name__ == "__main__":
    sum = Summoner("애극")
    #
    # url = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/%EB%AF%B8%EB%81%84%EB%A5%B4%EB%A5%B4?api_key=RGAPI-37384fa5-73b5-45ac-aeca-2c72560b52d3"
    # req = urllib.request.Request(url)
    # data = urllib.request.urlopen(req).read()
    # data = data.decode(encoding='UTF-8')
    # data = urllib.request.unquote(data)
    # print(data)
    #
