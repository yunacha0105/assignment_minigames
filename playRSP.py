import random

def playRSP():
    option = ['가위', '바위', '보']
    print('''가위바위보 게임을 시작합니다!''')
    while True:
        computer = random.choice(option)
        user = input('가위, 바위, 보 !!! (종료:q):')
        if user == 'q':
            break

        if user not in option:
            print('잘못 입력하셨습니다.')
            continue

        print(f'컴퓨터: {computer}')

        if user == computer:
            print('무승부!')
        elif (user == '가위' and computer == '보') or \
             (user == '바위' and computer == '가위') or \
             (user == '보' and computer == '바위'):
            print('승리!')
        else:
            print('패배!')
