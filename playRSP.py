import random

def playRSP():
    # 가위바위보 게임에서 나올 수 있는 선택지 정의
    option = ['가위', '바위', '보']
    print('''가위바위보 게임을 시작합니다! (3판 2선승제)''')

    win = 0
    lose = 0

    # 3판 2선승제 만들기
    while win < 2 and lose < 2:

        # 컴퓨터 가위 바위 보 중 랜덤 결정
        computer = random.choice(option)
        user = input('가위, 바위, 보 !!! (종료:q):')

        # 게임 나가는 법
        if user == 'q':
            break

        # 잘못 입력했을 경우
        if user not in option:
            print('잘못 입력하셨습니다.')
            continue

        # 컴퓨터 결과값 출력
        print(f'컴퓨터: {computer}')

        if user == computer:
            print('무승부!')

        elif (user == '가위' and computer == '보') or \
             (user == '바위' and computer == '가위') or \
             (user == '보' and computer == '바위'):
            print('승리!')
            win += 1

        else:
            print('패배!')
            lose += 1

        # 현재 결과값
        print(f'현재 결과: {win}승 {lose}패')

    # 최종 결과 및 점수
    if win == 2:
        print('최종 승리! + 50점 획득')
        return 50
    else:
        print('최종 패배! - 20점 차감')
        return -20