import urllib.parse
import ast
import re
import mycommunication
from urllib import request, parse

class Summoner:
    def __init__(self, name):
        self.summonerId = 0
        self.name = re.sub('[ ]', '', name).lower()

        if(type(self.name) is str):
            self.getSummonerInfo()
            self.getRank()
        else:
            return

    def getSummonerInfo(self):
        print("-소환사 정보-")

        url = "https://kr.api.riotgames.com/api/lol/KR/v1.4/summoner/by-name/{}?api_key=RGAPI-37384fa5-73b5-45ac-aeca-2c72560b52d3".format(urllib.request.quote(self.name))

        self.summonerData = mycommunication.inputUrlreturnDict(url)

        if(type(self.summonerData) is urllib.error.HTTPError):
            print("존재하지 않는 소환사")
            return

        self.summonerId = self.summonerData[self.name]['id']

        print(self.summonerData[self.name])



    def getRank(self):
        print("-2017 시즌 랭크 게임-")

        url = "https://kr.api.riotgames.com/api/lol/KR/v1.3/stats/by-summoner/{}/ranked?season=SEASON2017&api_key=RGAPI-37384fa5-73b5-45ac-aeca-2c72560b52d3".format(self.summonerId)

        self.seasonRankData = mycommunication.inputUrlreturnDict(url)

        if(type(self.seasonRankData) is urllib.error.HTTPError):
            print("랭크 기록이 없습니다")
            return

        print(self.seasonRankData['champions'])


if __name__ == "__main__":
    while True:
        sumName = input()
        sum = Summoner(sumName)