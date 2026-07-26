
import random

def playUpdown():
    answer = int(random.randint(1,50))
    print('''Up Down 게임을 시작합니다!
1 - 50 사이의 답을 맞춰보세요! (종료:q)''')
    while True:
        user_input = input(':')
        if user_input == 'q':
            break

        if int(user_input) not in list(range(1,51)):
            print('잘못 입력 했습니다.')
            continue

        if int(user_input) > answer:
            print('Down')

        elif int(user_input) < answer:
            print('Up')

        else:
            print('정답입니다 ~!')
            break