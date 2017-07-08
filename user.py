import urllib.parse
import ast
import re
import mycommunication
from urllib import request, parse

apiKey = "RGAPI-5fd912d9-7bb2-4910-b6fe-6da1f9277e00"


class Summoner:
    def __init__(self, name):
        self.summonerId = 0
        self.name = re.sub('[ ]', '', name).lower()
        self.totalRank = {}

        if(type(self.name) is str):
            self.getSummonerInfo()
            check = self.isRankPlayed()
            if(check is False):
                return
            self.getTier()
            self.getRankMost()
            self.getAll()
        else:
            return


    def isRankPlayed(self):
        url = "https://kr.api.riotgames.com/api/lol/KR/v1.3/stats/by-summoner/{}/ranked?season=SEASON2017&api_key={}".format(self.summonerId, apiKey)
        self.seasonRankData = mycommunication.inputUrlreturnDict(url)

        if(type(self.seasonRankData) is urllib.error.HTTPError):
            print("랭크 기록이 없습니다")
            return False
        else:
            return True


    def getSummonerInfo(self):
        print("-소환사 정보-")

        url = "https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(urllib.request.quote(self.name), apiKey)

        self.summonerData = mycommunication.inputUrlreturnDict(url)

        #존재하지 않는 소환사일 경우 404
        if(type(self.summonerData) is urllib.error.HTTPError):
            print("존재하지 않는 소환사")
            return

        self.summonerId = self.summonerData['id']

        print(self.summonerData)


    def getRankMost(self):
        i = 0
        print("-2017 시즌 랭크 게임 모스트-")
        mostCountArr = []
        mostArr = []

        #랭크 기록 리스트에 챔피언 '이름' 추가, 평점 추가. 모스트 픽 구하기 위해 경기 수 배열에 저장.
        for x in range(len(self.seasonRankData['champions']) -1):
            mostCountArr.append(self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'])
            if(self.seasonRankData['champions'][x]['id'] is 0):
                self.totalRank = self.seasonRankData['champions'][x]
                mostCountArr.pop(x)
            else:
                pass


        if(self.totalRank == {}):
            self.totalRank = self.seasonRankData['champions'][len(self.seasonRankData['champions']) -1]


        mostCountArr.sort(reverse=True)
        mostCountArr = mostCountArr[0:3]

        for x in range(len(mostCountArr)):
            if(len(mostArr) >= 9):
                break
            for y in range(len(self.seasonRankData['champions'] )-1):
                if(mostCountArr[x] == self.seasonRankData['champions'][y]['stats']['totalSessionsPlayed']):
                    mostArr.append(mycommunication.getChampionName(self.seasonRankData['champions'][y]['id']))
                    mostArr.append(round((self.seasonRankData['champions'][y]['stats']['totalChampionKills'] + self.seasonRankData['champions'][y]['stats']['totalAssists']) / self.seasonRankData['champions'][y]['stats']['totalDeathsPerSession'], 2))
                    mostArr.append(round(self.seasonRankData['champions'][y]['stats']['totalSessionsWon']/self.seasonRankData['champions'][y]['stats']['totalSessionsPlayed']*100))

        print(mostArr)


    def getTier(self):
        print("-티어-")

        url = "https://kr.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}".format(self.summonerId, apiKey)

        self.tier = mycommunication.tierDict(url)

        print(self.tier)


    def getAll(self):
        print("-2017 시즌-")
        self.allData = {}
        self.visionAvg = 0
        url = "https://kr.api.riotgames.com/api/lol/KR/v1.3/game/by-summoner/{}/recent?api_key={}".format(self.summonerId, apiKey)

        self.recendData = mycommunication.recnetDict(url)

        for x in range(len(self.recendData['games'])):
            self.visionAvg += self.recendData['games'][x]['stats']['visionScore']
        self.visionAvg = self.visionAvg / len(self.recendData['games'])

        self.allData['rate'] = round(self.totalRank['stats']['totalSessionsWon']/self.totalRank['stats']['totalSessionsPlayed'] * 100)
        self.allData['vision'] = self.visionAvg
        self.allData['score'] = round(((self.totalRank['stats']['totalChampionKills'] + self.totalRank['stats']['totalAssists']) / self.totalRank['stats']['totalDeathsPerSession']), 2)

        print(self.allData)



    def getRecent(self):
        pass

    def getCurr(self):
        pass




if __name__ == "__main__":
    while True:
        sumName = input()
        sum = Summoner(sumName)