import urllib.parse
import re
import mycommunication
import review
import pymysql
from urllib import request, parse
from collections import Counter

apiKey = "RGAPI-0f10c455-7071-46ec-9e93-0d1a688198bc"

tmp = pymysql.connect(host='localhost', user='root', password='', db='concretejungle', charset='utf8')
curs = tmp.cursor()


class Summoner:
    def __init__(self, name):
        self.summonerId = 0
        self.name = re.sub('[ `~!@#$%^&*()_+{}|[\:;<>,.?/\'\"＃＆＊＠§※☆★○●◎◇]', '', name).lower()
        self.totalRank = {}

        if(type(self.name) is str):
            if( self.getSummonerInfo() is False):
                return

            if(self.isRankPlayed() is False):
                return
            self.getCurr()
            self.getTier()
            self.getRankMost()
            self.getAll()

            self.allReview()
            self.championReview()

            dat = Database(self.summonerData, self.tier, self.mostArr, self.allData, self.playedChampion)

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

        url = "https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(urllib.request.quote(self.name), apiKey)

        self.summonerData = mycommunication.inputUrlreturnDict(url)

        #존재하지 않는 소환사일 경우 404
        if(type(self.summonerData) is urllib.error.HTTPError):
            print("존재하지 않는 소환사")

            return False

        self.summonerId = self.summonerData['id']

        return True

    def getRankMost(self):
        mostCountArr = []
        self.mostArr = []

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
            for y in range(len(self.seasonRankData['champions'] )-1):
                if(mostCountArr[x] == self.seasonRankData['champions'][y]['stats']['totalSessionsPlayed']):
                    self.mostArr.append(mycommunication.getChampionInfo(self.seasonRankData['champions'][y]['id'], apiKey)[0])
                    self.mostArr.append(round(self.seasonRankData['champions'][y]['stats']['totalSessionsWon'] / self.seasonRankData['champions'][y]['stats']['totalSessionsPlayed'] * 100))
                    self.mostArr.append(round((self.seasonRankData['champions'][y]['stats']['totalChampionKills'] + self.seasonRankData['champions'][y]['stats']['totalAssists']) / self.seasonRankData['champions'][y]['stats']['totalDeathsPerSession'], 2))
                    if (len(self.mostArr) >= 9):
                        break

        if (len(self.mostArr) < 9):
            for x in range(6):
                self.mostArr.append('-')
                if (len(self.mostArr) >= 9):
                    break

    def getTier(self):

        url = "https://kr.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}".format(self.summonerId, apiKey)

        self.tier = mycommunication.tierDict(url)

    def getAll(self):
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

        self.allData['W'] = self.totalRank['stats']['totalSessionsWon']
        self.allData['L'] = self.totalRank['stats']['totalSessionsLost']
        self.allData['Rate'] = round(self.totalRank['stats']['totalSessionsWon']/self.totalRank['stats']['totalSessionsPlayed'] * 100)
        self.allData['Vision'] = self.visionAvg
        self.allData['Score'] = round(((self.totalRank['stats']['totalChampionKills'] + self.totalRank['stats']['totalAssists']) / self.totalRank['stats']['totalDeathsPerSession']), 2)
        self.allData['Lane'] = self.position
        self.allData['Totem'] = self.totemChanged

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

    def getCurr(self):
        url = "https://kr.api.riotgames.com/observer-mode/rest/consumer/getSpectatorGameInfo/KR/{}?api_key={}".format(self.summonerId, apiKey)

        self.curr = mycommunication.inputUrlreturnDict(url)

        if(type(self.curr) is urllib.error.HTTPError):
            self.summonerData['current'] = 'No'

        else:
            for x in range(len(self.curr['participants'])):
                if (self.curr['participants'][x]['summonerName'] == self.summonerData['name']):
                    self.summonerData['current'] = mycommunication.getChampionInfo(self.curr['participants'][x]['championId'], apiKey)[0]
                    break

    def championReview(self):
        self.playedChampion = []
        champion = []

        for x in range(len(self.seasonRankData['champions'])):

            if(self.seasonRankData['champions'][x]['id'] is 0):
                continue
            else:
                #i = len(self.playedChampion) - 1
                self.playedChampion.append(mycommunication.getChampionInfo(self.seasonRankData['champions'][x]['id'], apiKey))

                try:
                    self.playedChampion[x].append(round(self.seasonRankData['champions'][x]['stats']['totalSessionsWon'] / self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'] * 100))
                except:
                    self.playedChampion[x-1].append(round(self.seasonRankData['champions'][x]['stats']['totalSessionsWon'] / self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'] * 100))

                if (self.seasonRankData['champions'][x]['stats']['totalDeathsPerSession'] != 0):
                    try:
                        self.playedChampion[x].append(round((self.seasonRankData['champions'][x]['stats']['totalChampionKills'] + self.seasonRankData['champions'][x]['stats']['totalAssists']) / self.seasonRankData['champions'][x]['stats']['totalDeathsPerSession'], 2))
                    except:
                            self.playedChampion[x-1].append(round((self.seasonRankData['champions'][x]['stats']['totalChampionKills'] + self.seasonRankData['champions'][x]['stats']['totalAssists']) / self.seasonRankData['champions'][x]['stats']['totalDeathsPerSession'], 2))
                else:
                    try:
                        self.playedChampion[x].append('Perfect')
                    except:
                        self.playedChampion[x-1].append('Perfect')

                try:
                    self.playedChampion[x].append(self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'])
                except:
                    self.playedChampion[x-1].append(self.seasonRankData['champions'][x]['stats']['totalSessionsPlayed'])


        self.playedChampion = review.review(self.playedChampion)

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


        self.allData['comment'] = self.allReviewString
        self.allData['grade'] = score


class Database:
    def __init__(self, summoner, tier, most, season, champion):

        self.summoner = summoner
        self.tier = tier
        self.most = most
        self.season = season
        self.champion = champion

        sql = """
        select exists (select * from userinfo where name = %(이름)s ) as success
        """
        curs.execute(query=sql, args={'이름': self.summoner['name']})


        if(curs.fetchone()[0] == 0):
            self.insert()
            print("추가")
        else:
            self.update()
            print("데이터 베이스에 존재함.")

        tmp.commit()

    def insert(self):
        sql = """
        insert into userinfo (`name`, `summonerId`, `accountId`, `current`, `leagueName` ,`tier`, `rank`, `leaguePoints`,`veteran`, `most1`, `most1Rate`, `most1kda`, `most2`, `most2Rate`,
        `most2kda`, `most3`, `most3Rate`, `most3kda`, `W`, `L`, `Rate`, `Score`, `Lane`, `Totem`, `Comment`, `Grade`)
        values( %(name)s, %(summonerId)s, %(accountId)s, %(current)s, %(leagueName)s, %(tier)s, %(rank)s, %(leaguePoints)s, %(veteran)s, %(most1)s, %(most1Rate)s, %(most1kda)s, %(most2)s,
        %(most2Rate)s, %(most2kda)s, %(most3)s, %(most3Rate)s, %(most3kda)s, %(W)s, %(L)s, %(Rate)s, %(Score)s, %(Lane)s, %(Totem)s, %(Comment)s, %(Grade)s)
        """

        curs.execute(query=sql, args={'name': self.summoner['name'], 'summonerId': self.summoner['id'], 'accountId': self.summoner['accountId'],
                                      'leagueName':self.tier['leagueName'], 'current':self.summoner['current'], 'tier':self.tier['tier'], 'rank':self.tier['rank'], 'leaguePoints':self.tier['leaguePoints'],'veteran':self.tier['veteran'],
                                      'most1':self.most[0], 'most1Rate':self.most[1], 'most1kda':self.most[2], 'most2':self.most[3], 'most2Rate':self.most[4],
                                      'most2kda':self.most[5], 'most3':self.most[6], 'most3Rate':self.most[7], 'most3kda':self.most[8], 'W':self.season['W'],
                                      'L':self.season['L'], 'Rate':self.season['Rate'], 'Score':self.season['Score'], 'Lane':self.season['Lane'], 'Totem':self.season['Totem'],
                                      'Comment':self.season['comment'], 'Grade':self.season['grade']})


        sql = """
        insert into playedchampion (`Name`, `Champion`, `Rate`, `Score`, `Games`, `Comment`)
        values (%(Name)s, %(Champion)s, %(Rate)s, %(Score)s, %(Games)s, %(Comment)s)
        """

        for x in range(len(self.champion)):
            curs.execute(query=sql, args={'Name': self.summoner['name'], 'Champion': self.champion[x][0], 'Rate': self.champion[x][2], 'Score':self.champion[x][3], 'Games':self.champion[x][4], 'Comment':self.champion[x][5]})

    def update(self):

        sql = """
        update userinfo set `current` = %(current)s, `leagueName` = %(leagueName)s, `tier` = %(tier)s, 
        `rank` = %(rank)s, `leaguePoints` = %(leaguePoints)s,  `veteran` = %(veteran)s, 
        `most1` = %(most1)s, `most1Rate` = %(most1Rate)s, `most1kda` = %(most1kda)s,
        `most2` = %(most2)s, `most2Rate` = %(most2Rate)s, `most2kda` = %(most2kda)s,
         `most3` = %(most3)s, `most3Rate` = %(most3Rate)s, `most3kda` = %(most3kda)s,
         `W` = %(W)s, `L` = %(L)s, `Rate` = %(Rate)s, `Score` = %(Score)s, `Lane` = %(Lane)s,
         `Totem` = %(Totem)s, `Comment` = %(Comment)s, `Grade` = %(grade)s where `name` = %(Name)s
        """

        curs.execute(query=sql, args={'current':self.summoner['current'], 'leagueName':self.tier['leagueName'], 'tier': self.tier['tier'],
                                      'rank':self.tier['rank'], 'leaguePoints':self.tier['leaguePoints'],'veteran':self.tier['veteran'], 'most1':self.most[0], 'most1Rate':self.most[1],
                                      'most1kda': self.most[2], 'most2':self.most[3], 'most2Rate':self.most[4], 'most2kda':self.most[5],
                                      'most3':self.most[6], 'most3Rate':self.most[7], 'most3kda':self.most[8], 'W':self.season['W'],
                                      'L':self.season['L'], 'Rate':self.season['Rate'], 'Score':self.season['Score'],
                                      'Lane':self.season['Lane'], 'Totem':self.season['Totem'], 'Comment':self.season['comment'],
                                      'grade':self.season['grade'], 'Name':self.summoner['name']})


        sql = """
        delete from playedchampion where Name = %(Name)s
        """

        curs.execute(query=sql, args={'Name':self.summoner['name']})


        sql = """
        insert into playedchampion (`Name`, `Champion`, `Rate`, `Score`, `Games`, `Comment`)
        values (%(Name)s, %(Champion)s, %(Rate)s, %(Score)s, %(Games)s, %(Comment)s)
        """

        for x in range(len(self.champion)):
            curs.execute(query=sql, args={'Name': self.summoner['name'], 'Champion': self.champion[x][0], 'Rate': self.champion[x][2], 'Score':self.champion[x][3], 'Games':self.champion[x][4], 'Comment':self.champion[x][5]})




if __name__ == "__main__":

    while True:
        sumName = input()
        sum = Summoner(sumName)
        del sum