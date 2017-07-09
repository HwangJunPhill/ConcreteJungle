def review(list):
    review = []

    for x in range(len(list)):
        string = ""
        #전사
        #
        if list[x][0] == "가렌":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "티모도 찢을 실력이군요. 짝짝짝."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "W와 패시브, 탱킹 능력을 활용한 무장색 패기."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "텔타고 로밍와서 점화걸린 딸피 적한테 궁박고 집감."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "궁 딜계산 못해서 맨날 어시만 먹음"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "제발 앞라인 때리지 말고 딜러좀 물어봐요."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "뒤에서 깔짝대다 악당 딸피되면 풀발해서 달려들어 킬함."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "극딜 가렌 매드무비가 롤을 망쳤음. "
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "왜 점멸 Q로 탱커물다가 짤려놓고 아군 탓 하는거죠?"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "왜 W 쿨 도는걸 본적이 없지.."

        elif list[x][0] == "갱플랭크":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "그라가스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "나르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "나서스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "다리우스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "진정한 탑솔러를 목도하라."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "Q 한바퀴 돌면 피흡오져서 더욱 듬직한형."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "궁 쓰다가 뒤질거 뻔하니까 그냥 몸만 대세요."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "한타때 궁킬딸 씹오짐."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "궁으로 킬하면 미니언 공포걸리는게 멋있다구요? 그럼 궁으로 킬을 해보세요. 궁으로 실피만들고 패시브로 잡지말고."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "E로 미니언만 끌어옴. ㄹㅇ 블츠보다 효율 좋음."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "갱 온 정글러까지 더블킬을 더블로 땄는데 아래쪽 다 터져있음."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "어떤 상황이라도 5스택 아니면 궁 안씀."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "제발 궁 믿고 라인 밀지 마세요; 갱오면 궁 쓰기 전에 죽잖아요."

        elif list[x][0] == "다이애나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "럼블":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "레넥톤":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "렉사이":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "리신":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "리븐":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "모데카이저":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "문도 박사":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "바이":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "볼리베어":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "쉬바나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "한타때 이니쉬 진짜 오지네요. "
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "정글링 속도 빠름 빠름 빠름"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "피갈퀴손 - 몰락 - 광전사 - 팬댄 - 트포 - 마법사의 최후"

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "제발 먼저 들어가 쉬바나..."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "동족을 보호하려는 생각이 아주 깊군요. 용을 한대도 때리지 않다니. "
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "갱올때 W키고 걸어옴"

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "몸만 탱탱하고 쓸모가 없음."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "궁으로 벽에 머리 박는게 취미."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "W 키고 라인밀다가 짤리는게 특기."

        elif list[x][0] == "스카너":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "신 짜오":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아트록스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "야스오":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "오공":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "올라프":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "요릭":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "우디르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "워윅":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "이렐리아":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "일라오이":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "잭스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "제이스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "카밀":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "케일":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "클레드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "트런들":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "트린다미어":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "판테온":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "피오라":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "헤카림":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass


        #암살자

        #
        elif list[x][0] == "녹턴":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "불끄면 선취점"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "혼자 남은줄 알았는데 둘이네? 그럼 너도 죽어. 더블킬! "
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "딜갔는데 팀원들이 자꾸 이니쉬 걸으래.."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "W 쓰고 무빙침."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "Q위에 올라가면 공격력 이속 오르는거 모르죠?"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "미니언에 공포 좀 걸지 말아봐요."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "궁 데미지 보다 피가 적은 적 아니면 궁 안씀. "
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "님 왜 W로 이즈 Q 막음?"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "님 왜 궁쓰고 걸어감?"

        elif list[x][0] == "니달리":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "렝가":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "르블랑":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "마스터 이":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "알파 한번에 cc기 세개 궁 두개 피함."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "그래도 방템 한두개 감."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "정글 만 돔 → 카정당함 → 열심히 정글만 돔 → 적 정글 전장의 화신 → 그러나 아군 캐리로 승리 → 적군 싸우는거 정글몹 먹으면서 구경함."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "킬 먹고 명캔한다고 깝치다가 평타랑 명상 둘다 못씀. "
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "캐리도 하고 똥도 싸는 마스터 이. (똥 싸는 횟수 >>> 캐리하는 횟수)"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "아군 : 벌레가 겹눈이 많아서 징그럽네."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "한타가 뭐임?"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "알파로 스킬 씹히는거 모름. 포탑 어그로 끌렸을때 달려나가다가 포탑 사거리 안에서 명상씀. "
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "정글에서 적군 발견하면 일단 요우무 + 궁 + E 키고 달려감. 죽으러 달려가는 거임."

        elif list[x][0] == "샤코":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아칼리":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "에코":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "이블린":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "제드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "비술의 검 없어진게 아쉽네요ㅠ"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "히드라 간다음에 스플릿함."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "원딜 짜르고 같이 죽음."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "닿으면 녹음. 물론 제드가."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "표창 두개 이상 맞출줄 모름."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = " 요우무 W W 점멸 궁으로 이니쉬 열고 사망."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "부쉬에 숨어 있다가 킬딸 하고 다시 부쉬 들어감."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "바로 앞에서도 표창 못맞추는데 그냥 E선마 하시는게 나을듯."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "약자 멸시 있는데도 막타를 놓치네 ㅋㅋㅋㅋ"

        elif list[x][0] == "카사딘":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "카직스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "한타 6단 점프가 취미."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "점프하면 킬."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "도약 후 원딜한테 Q 긁고 죽음."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "미드 밀때 킬하러 다른 라인 감. 바론 먹을 때 킬하러 다른 라인 감. 다른 라인 감. 다른 라인.."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "아군 갱 요청 무시하고 적 정글에 살다가 백업온 적군한테 여러번 뒤지고 게임 터짐."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "6렙 11렙 16렙때 실수로 E찍고 그 다음 레벨에 진화함."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "고립 아니면 안싸움."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "여눈 가지 마세요 제발.. 적 유닛 없으면 W랑 E로 쌓을거에요?"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "님 진화 할줄 알죠? 아는데 왜그러지.."

        #
        elif list[x][0] == "카타리나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "펜타여신"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "한타여신"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "순보로 들어가서 어그로 끌고 존야 쓰면 아군이 마무리해줌."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "킬딸여왕"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "혼자 멀찍이 들어감 → 물려서 짤림 → 근처에 도망가던 아군한테 왜 순보 사거리 안주냐고 욕함"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "칼 주우면 순보 쿨 줄어들어요."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "신나게 킬처먹고 놀다가 맨날 중요한 순간에 짤려서 게임 짐."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "이제 와드에 순보 못타요. 바뀐지가 언젠데."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "칼 들었다고 ad 가는거 아니죠?"

        elif list[x][0] == "탈론":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "피즈":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass



        #마법사
        elif list[x][0] == "라이즈":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "럭스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "리산드라":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "말자하":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "모르가나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "베이가":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "벨코즈":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "브랜드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "블라디미르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "빅토르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "스웨인":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "신드라":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아리":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아우렐리온 솔":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아지르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "애니":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "최소 3인궁"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "Q를 활용해 라인전 마나 관리 및 갱호응 잘함"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "궁 박고 뒤지면 티버가 캐리해줌"

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "솔직히 애니는 티버가 다 해먹는듯."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "적군 두명 이상 아니면 궁 안씀. 1 대 1 상황에서도 마찬가지. 그런데 정작 2인궁 못맞춤"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "라인전에서 패시브 스택 다 쌓으면 적 챔피언 아니면 절대 스킬 안씀. "

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "애니가 티버랑 백도어 하는 챔피언 인가요?"
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "애니는 탱커가 아니니 용암 '방패'는 필요 없다."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "티버 어떻게 움직이는지 알고 있죠?"

        elif list[x][0] == "애니비아":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "엘리스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "오리아나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "자이라":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "제라스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "직스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "카르마":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "카서스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "가게 두어라."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "세 네번중에 한번 Q 가운데 맞춤."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "W깔고 E키고 비비면 아군이 한타 이겨놓음."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "Q 테두리 잘 맞춤."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "아군이 싸운다 싶으면 그거 보다가 짤리고 패시브 상태에서 궁 씀. 궁 세번당 1킬 정도 함."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "Q는 맞출줄 모르는데 E키고 잘 적한테 대줌."

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "포탑 미는거보다 멀리서 궁으로 킬딸하는게 더 죠아 ㅎㅎ."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "카서스는 죽고 나서 패시브일때 프리딜 넣을 수 있어서 일단 시작하면 죽고 보자는것이 신조."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "여눈 쌓다 보면 게임 끝나 있음."

        elif list[x][0] == "카시오페아":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "케넨":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "탈리야":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        #
        elif list[x][0] == "트위스티드 페이트":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    string = "대충 Q 날려도 적군 두명 맞춤."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "로밍 성공률 80%정도 되겠네요."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "골카 맞추고 짤리면 아군이 대신 죽여줌."

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    string = "온 신경을 집중해서 Q 날려야 가끔 한두명 맞는다니.. 골카를 맞추고 Q를 날리세요."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "어떻게 골카 맞추고 Q를 못맞출 수가 있죠?"
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "봇 로밍각 나옴 → 일단 궁 탐 → 평 평 블루카드 → 핑 튀었다고 핑계댐"

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    string = "이건 진짜 아군이 트롤인거."
                elif list[x][3] >= 2 and list[x][3] < 3:
                    string = "라인정리는 레드카드로 하는거에요. 블루카드 말구요."
                elif list[x][3] >= 0 and list[x][3] < 2:
                    string = "궁 쓰고 있는데 자기가 맞고 있는줄 모름. 궁 타고 도착하면 딸피에 점화걸려있음. "

        elif list[x][0] == "피들스틱":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "하이머딩거":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass


        #서포터
        elif list[x][0] == "나미":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "누누":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "라칸":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "룰루":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "바드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "브라움":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "소나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "소라카":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "쓰레쉬":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아이번":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "잔나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "질리언":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "타릭":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "탐 켄치":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass


        #탱커
        elif list[x][0] == "갈리오":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "노틸러스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "람머스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "레오나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "마오카이":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "말파이트":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "블리츠크랭크":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "뽀삐":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "사이온":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "세주아니":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "신지드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "쉔":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "아무무":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "알리스타":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "자르반 4세":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "자크":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "초가스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass



        #원딜
        elif list[x][0] == "그레이브즈":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "드레이븐":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "루시안":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "미스포츈":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "바루스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "베인":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "시비르":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "애쉬":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "우르곳":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "이즈리얼":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "자야":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "진":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "징크스":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "칼리스타":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "케이틀린":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "코그모":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "코르키":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "퀸":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "킨드레드":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "트리스타나":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "트위치":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        elif list[x][0] == "티모":

            if list[x][2] <= 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] >= 50 and list[x][2] < 60:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

            elif list[x][2] < 50:
                if list[x][3] >= 3:
                    pass

                elif list[x][3] >= 2 and list[x][3] < 3:
                    pass
                elif list[x][3] >= 0 and list[x][3] < 2:
                    pass

        list[x].append(string)

    return list