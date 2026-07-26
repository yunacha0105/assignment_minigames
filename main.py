from playBlackjack import playBlackjack
from playDungeon import playDungeon
from playSlimeRPG import playSlimeRPG
from playLotto import playLotto
from playRSP import playRSP
from playUpdown import playUpdown


score = 0
play_count = 0
win_count = 0

while True:
    # 메뉴출력
    print(f'''==================
         게임 메뉴
    ==================
    1. 업다운 게임
    2. 가위바위보 게임
    3. 로또 번호 출력
    4. 슬라임 RPG
    5. 던전 탐험 게임
    6. 블랙잭 21 게임
    7. 나가기
    ''')

    #메뉴 입력 받기
    menu = input(f'''현재 점수: {score}
총 플레이 횟수: {play_count}
플레이하고 싶은 게임의 메뉴를 입력하세요.
    : ''')

    if menu == '1':
        # 함수 결과 받아오기
        result = playUpdown()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    elif menu == '2':
        # 함수 결과 받아오기
        result = playRSP()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    elif menu == '3':
        # 함수 결과 받아오기
        result = playLotto()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    elif menu == '4':
        # 함수 결과 받아오기
        result = playSlimeRPG()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    elif menu == '5':
        # 함수 결과 받아오기
        result = playDungeon()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    elif menu == '6':
        # 함수 결과 받아오기
        score += playBlackjack()
        play_count += 1

        # 승리 판별법
        if result > 0:
            win_count += 1

        # 점수 입력
        score += result

    # 게임 종료시 결과 출력
    elif menu == '7':
        print(f'''=======================
       최종 결과
=======================
 총 : {play_count} 회
 승리 : {win_count} 회
 총점 : {score}''')
        break
    else:
        print('잘못입력하셨습니다.')
        continue