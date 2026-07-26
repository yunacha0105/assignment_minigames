
import random

def playUpdown():

    # 1 - 50 중 랜덤 문제 출제
    answer = int(random.randint(1,50))
    print('''Up Down 게임을 시작합니다!
1 - 50 사이의 답을 맞춰보세요! (종료:q)''')

    while True:

        # 유저 입력값
        user_input = input(':')

        # 게임 종료
        if user_input == 'q':
            break

        # 잘못 입력 시
        if not user_input.isdigit():
            print('잘못 입력 했습니다.')
            continue

        user_input = int(user_input)

        if user_input < 1 or user_input > 50:
            print('1부터 50까지의 숫자를 입력하세요.')
            continue

        if user_input > answer:
            print('Down')

        elif user_input < answer:
            print('Up')

        else:
            print('정답입니다 ~! + 20점 획득')
            return 20
            break