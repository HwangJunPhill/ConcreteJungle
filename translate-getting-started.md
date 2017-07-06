Getting Started
===============

이 가이드를 접하기 전에, 우리는 JSON, OOP와 조금 더 친해지기를 추천합니다.
이 문서는 Riot Games API에 대한 기초적인 이해를 제공합니다.
당신이 탐험을 시작하고 API를 사용해 최대한 빨리 개발할 수 있도록 설계되어 있습니다.
우린 당신이 만드는 것을 기다릴수 없어요!


Registring for the Riot Games API
---------------------------------

Riot Games API를 시작하기 전에 반드시 League of Legneds 계정을 생성해야 합니다.
계정을 생성할 때, 개발자 포털 계정이 당신을 위해 추가됩니다. (계정과 관련된 개발 API 키 생성)
당신의 계정은 또한 너의 어플리케이션과 용법, 그리고 그의 반대와 관련된 우리의 팀과 의사소통을 허가받습니다.
API keys에 대한 더 많은 정보와 API Keys 문서를 보기 위해서입니다.
모든 Riot Game API 리퀘스트는 API Key를 필요로 한다는 것을 메모하고, 
당신은 반드시 각각의 api_key 파라미터 요청에 API key를 사용해야 합니다.

```
https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=<key>
```

<key> 부분을 당신의 API key로 바꿔야 한다는 사실을 잊지마세요.
더 많은 정보와 예제는, API Reference 페이지에서 API 실행을 시도하세요.


Hello, World!
-------------

놀라운걸 만드는 가장 빠른 길은 가능한 가장 간단한 예제를 보는 것 입니다.
아래의 cURL 요청은 RiotSchmick의 기본 소환사 정보를 JSON으로 불러옵니다.

```
curl --request GET 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=<key>' --include
```

<key> 부분을 당신의 API key로 바꿔야 한다는 사실을 잊지마세요.
cURL은 없는데 이걸 시도해 보고 싶으시다면 그저 브라우저에 복붙해 넣으세요.


VALIDATING CALLS
----------------

