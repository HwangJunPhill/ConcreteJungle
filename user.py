import urllib.parse
import re
import mycommunication
import review
from urllib import request, parse
from collections import Counter


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
            self.allReview()
            self.championReview()
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
                    mostArr.append(mycommunication.getChampionInfo(self.seasonRankData['champions'][y]['id'], apiKey)[0])
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
        self.visionAvg = 0.0
        self.position = []
        self.totemChanged = 0
        url = "https://kr.api.riotgames.com/api/lol/KR/v1.3/game/by-summoner/{}/recent?api_key={}".format(self.summonerId, apiKey)

        self.recendData = mycommunication.recnetDict(url)


        for x in range(len(self.recendData['games'])):
            self.visionAvg += self.recendData['games'][x]['stats']['visionScore']

            try:
                self.position.append(self.recendData['games'][x]['stats']['playerPosition'])
            except KeyError:
                continue

            try:
                if(self.recendData['games'][x]['stats']['item6'] != 3340):
                    self.totemChanged += 1
            except KeyError:
                    continue


        self.position = self.calLane(self.position)
        self.visionAvg = self.visionAvg / len(self.recendData['games'])
        self.totemChanged = round((self.totemChanged / len(self.recendData['games'])) * 100)

        self.allData['Rate'] = round(self.totalRank['stats']['totalSessionsWon']/self.totalRank['stats']['totalSessionsPlayed'] * 100)
        self.allData['Vision'] = self.visionAvg
        self.allData['Score'] = round(((self.totalRank['stats']['totalChampionKills'] + self.totalRank['stats']['totalAssists']) / self.totalRank['stats']['totalDeathsPerSession']), 2)
        self.allData['Lane'] = self.position
        self.allData['Totem'] = self.totemChanged

        print(self.allData)


    def calLane(self, position):
        position = Counter(position)
        position = position.most_common()

        if(position[0][0] == 1):
            return "top"
        elif(position[0][0]== 2):
            return  "mid"
        elif(position[0][0]==3):
            return "jungle"
        elif(position[0][0]==4):
            return "bot"


    def getRecent(self):
        #게임중이면 championReview 아님 return
        pass


    def getCurr(self):
        pass


    def championReview(self):
        self.playedChampion = []
        champion = []

        for x in range(len(self.seasonRankData['champions']) -1):
            if(self.seasonRankData['champions'][x]['id'] is 0):
                continue
            else:
                champion.append(mycommunication.getChampionInfo(self.seasonRankData['champions'][x]['id'], apiKey))
                champion[x].append(round((self.seasonRankData['champions'][x]['stats']['totalChampionKills'] +
                                       self.seasonRankData['champions'][x]['stats']['totalAssists']) /
                                      self.seasonRankData['champions'][x]['stats']['totalDeathsPerSession'], 2))
                champion[x].append(round(self.seasonRankData['champions'][x]['stats']['totalSessionsWon'] /
                                      self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'] * 100))

                self.playedChampion.append(champion)

        self.playedChampion = review.review(self.playedChampion)
        print(self.playedChampion)


    def allReview(self):
        self.allReviewString = ""
        score = 0
        if(self.allData['Rate'] >= 65):
            self.allReviewString += "음.. 승률은 이정도면 조금 높네요. "
            score += 5

            if(self.allData['Score'] >= 6):
                self.allReviewString += "그런데 평점 뭐지. "
                score += 5
            elif(self.allData['Score'] >= 4 and self.allData['Score'] < 6):
                self.allReviewString += "그래. 이정도 평점은 나와야 승률 저 정도 할 자격있어요. "
                score += 4
            elif(self.allData['Score'] >= 3 and self.allData['Score'] < 4):
                self.allReviewString += "이상하네 지 실력으로 이긴거라니; 신고할게요 헬퍼로? "
                score += 3
            elif(self.allData['Score'] >= 2 and self.allData['Score'] < 3):
                self.allReviewString += "좋죠? 킬관여 좀 하면 좀 이기고 그러니까? 그죠? 롤이 쉽죠 아주? 에휴 요즘에나 이렇지 옛날에 블츠 그랩이 타겟팅이었을 때 였어봐.  "
                score += 2
            elif(self.allData['Score'] >= 1 and self.allData['Score'] < 2):
                self.allReviewString += "버스 운전하는 횟수보단 타는 횟수가 한 다섯배 정도 높은거네 이건. 버스카드 자주자주 충전 해야 겠어요? "
                score += 1
            elif(self.allData['Score'] >= 0 and self.allData['Score'] < 1):
                self.allReviewString += "이런 세상에 쓸모가 하나도 없는 핵폐기물급 평점으로 이런 승률 어떻게 기룍해요??  "
                score += 0


        elif(self.allData['Rate'] >= 50 and self.allData['Rate'] < 65):
            self.allReviewString += "어쭈..ㅋ 가끔, 아니 자주 캐리받고 겨우겨우 승률 50퍼 넘기네. "
            score += 3
            if(self.allData['Score'] >= 6):
                self.allReviewString += "평점은 하늘을 뚫다못해 하늘나라 옥황상제 전립선을 찌르는데 승률이 왜 이거밖에.. 팀운 애도 ▶◀ "
                score += 5
            elif(self.allData['Score'] >= 4 and self.allData['Score'] < 6):
                self.allReviewString += "근데 평점은... 자주 캐리받는다는 말 취소. "
                score += 4
            elif(self.allData['Score'] >= 3 and self.allData['Score'] < 4):
                self.allReviewString += "곧 자기 티어 벗어날거 같죠? 절대 아니에요. 제발 꿈 깨세요. 님 이긴만큼 또 져요. 뭘 바래요 진짜. "
                score += 3
            elif(self.allData['Score'] >= 2 and self.allData['Score'] < 3):
                self.allReviewString += "승률 50퍼 넘기기 위해서 했던 노력이 눈에 선하네요. 피똥싸면서 롤했겠지.. 참 딱하군요.. 그 노력의 절반만 공부했어도 효도 했을 텐데. 눈물이 앞을 가리네요. 아 물론 효도는 묫자리를 좋은.. 아니다. "
                score += 2
            elif(self.allData['Score'] >= 1 and self.allData['Score'] < 2):
                self.allReviewString += "님보다 한 대여섯배 잘하는 친구한테 먹을거 바치고 비위 맞춰주면서 힘겹게 듀랭 뛸 기회 있을 때만 롤 하죠? "
                score += 1
            elif(self.allData['Score'] >= 0 and self.allData['Score'] < 1):
                self.allReviewString += "근데 평점은... 자주 캐리받는다는 말 취소. "
                score += 0

        elif(self.allData['Rate'] < 50):
            self.allReviewString += "아니 ㅋㅋㅋ 승률이.. 반타작도 못하는데 왜 랭뛰는거지..; "
            score += 1

            if(self.allData['Score'] >= 6):
                self.allReviewString += "일부로 티어 낮추고 킬만 처먹고 아무것도 안하죠? 진짜 쓰레기다. "
                score += 5
            elif(self.allData['Score'] >= 4 and self.allData['Score'] < 6):
                self.allReviewString += "양학하려고 왔는데도 평점 6점을 못넘기고 그래요? 한심하다 한심해. 롤 접어요 진짜. "
                score += 4
            elif(self.allData['Score'] >= 3 and self.allData['Score'] < 4):
                self.allReviewString += "평점 관리 하지마요 진짜 ㅋㅋㅋ 어차피 님 전적 누가 검색해 봐도 잘한다는 생각 안해요. 그런 생각 하는게 초딩이지. 그리고 픽창에서 잘하는척 하지 마요. 이건 진심으로 하는 충고에요. 개쪽당할거에요. "
                score += 3
            elif(self.allData['Score'] >= 2 and self.allData['Score'] < 3):
                self.allReviewString += "자기는 현지인 아니라는 생각을 가졌을 거라는게 진짜 너무 뻔하네요. 더럽고 끔찍하고 추악하고 혐오스러워요. 자기 주제를 알아야죠. "
                score += 2
            elif(self.allData['Score'] >= 1 and self.allData['Score'] < 2):
                self.allReviewString += "뭔 말을 하고 싶어도 한숨밖에 안나오네요 진짜. 에휴. 던지는척 하지 마요. 실력인거 다 아니까. 제발 롤 접어요. "
                score += 1
            elif(self.allData['Score'] >= 0 and self.allData['Score'] < 1):
                self.allReviewString += "진짜 롤의 암세포적인 존재. "
                score += 0

        self.allReviewString += "\n"

        if(self.allData['Totem'] >= 70):
            self.allReviewString += "장신구 꽤 자주 바꾸는 것 같고. "
            score += 5
            if(self.allData['Vision'] >= 20000):
                self.allReviewString += "맵 상태 좀 좋겠네. "
                score += 5
            elif(self.allData['Vision'] >= 15000 and self.allData['Vision'] < 20000):
                self.allReviewString += "하.. 자주 바꾸면 뭐해. 장신구 좀 자주 씁시다? 기껏 바꿨는데 썩혀두면 안좋잖아요? "
                score += 3
            elif(self.allData['Vision'] < 15000):
                self.allReviewString += "뒤지게 쳐맞아야 정신차리죠? 아이템 바꿀줄은 알고 쓸줄은 몰라요? 4번 키 빠졌어요? 해커가 해킹하고 장신구 단축키 바꿔놨어요? "
                score += 1
        elif (self.allData['Totem'] >= 50 and self.allData['Totem'] < 70):
            self.allReviewString += "한 30분쯤에 팀원이 패드립 섞어가면서 장신구 바꾸라고 하면 그때서야 바꾸는 타입인가. "
            score += 3

            if(self.allData['Vision'] >= 20000):
                self.allReviewString += "그래도 시야 장악 할건 하나 보네요. "
                score += 5
            elif(self.allData['Vision'] >= 15000 and self.allData['Vision'] < 20000):
                self.allReviewString += "잘 바꾸지도 않는데 잘 박지도 지우지도 않으면 뭐..  "
                score += 3
            elif(self.allData['Vision'] < 15000):
                self.allReviewString += "근데 님 신기한거 알려줄까요? 미니맵은 안보이는데 님이 시야 없는 곳에서 짤리는 장면은 보여요.  "
                score += 1

        elif (self.allData['Totem'] < 50):
            self.allReviewString += "그리고 죄송한데, 19렙이 아니라 9렙부터 장신구 바꿀 수 있어요. 모르는거 같아서요. "
            score += 1

            if(self.allData['Vision'] >= 20000):
                self.allReviewString += "그나저나 와드 막타 진짜 잘 치나 보다 ㅋㅋㅋ "
                score += 5
            elif(self.allData['Vision'] >= 15000 and self.allData['Vision'] < 20000):
                self.allReviewString += "설정에서 미니맵 크기라도 최소로 하고 해요. 어차피 어두워서 보이지도 않을거 화면이라도 안가리게 "
                score += 3
            elif(self.allData['Vision'] < 15000):
                self.allReviewString += "리 신인가요? 앞이 보이지 않아도 불편할게 없다면 뭐 냅둘게요. "
                score += 1


                #평타면 가끔 시야때문에 팀원들이랑 싸우지? 그전에 니가 잘 좀 해봐
                #하타면 설정에서 미니맵 크기라도 최소로 하고 해요. 어차피 어두워서 보이지도 않을거 화면이라도 안가리게


        self.allReviewString += "\n총평 : "
        if(score == 20):
            if(self.allData['Lane'] == "mid"):
                self.allReviewString += "오졌다. "
            elif(self.allData['Lane'] == "top"):
                self.allReviewString += "탑 캐리. "
            elif(self.allData['Lane'] == 'bot'):
                self.allReviewString += "봇이 잘하면 할게 없죠. "
            elif(self.allData['Lane'] == 'jungle'):
                self.allReviewString += "협곡갓. "

        elif(score >= 13 and score < 20):
            if(self.allData['Lane'] == "mid"):
                self.allReviewString += "제발 상대 cc기랑 니 딜 생각하고 깝쳐. "
            elif(self.allData['Lane'] == "top"):
                self.allReviewString += "탑신병자. "
            elif(self.allData['Lane'] == 'bot'):
                self.allReviewString += "그렇게 할거면 왜 봇가는지 정말 이해가 안된다. "
            elif(self.allData['Lane'] == 'jungle'):
                self.allReviewString += "양심적으로 블루는 미드 줘요. "
        elif(score >= 7 and score < 13):
            if(self.allData['Lane'] == "mid"):
                self.allReviewString += "딱 봐도 두려움 따윈 없는 개씹무리충. "
            elif(self.allData['Lane'] == "top"):
                self.allReviewString += "탑에서 좀 내려 옵시다. "
            elif(self.allData['Lane'] == 'bot'):
                self.allReviewString += "서로 싸우고 다른라인에 민폐 끼치지 마요. "
            elif(self.allData['Lane'] == 'jungle'):
                self.allReviewString += "갱승이라도 안 당하면 다행이지. "
        elif(score > 0 and score < 7):
            if(self.allData['Lane'] == "mid" or self.allData['Lane'] == 'top'):
                self.allReviewString += "이딴 쓰레기같은 실력으로 라인 잡지 마. "
            elif(self.allData['Lane'] == 'bot'):
                self.allReviewString += "라인전때 적 더블킬 !을 몇번 보게 될까. "
            elif(self.allData['Lane'] == 'jungle'):
                self.allReviewString += "정글몹 >>>> 님. "



        print(self.allReviewString)


if __name__ == "__main__":
    while True:
        sumName = input()
        sum = Summoner(sumName)