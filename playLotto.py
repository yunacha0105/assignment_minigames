import random

def playLotto():
    lotto = random.sample(range(1, 45), 6)
    print('로또를 구매합니다. 1부터 50까지 숫자 중 8개를 입력하시오.')

    while True:
        user = list(map(int, input('''예시) 1 20 43 7 9 15 23 8 
:''').split()))
        count = 0
        for num in user:
            if num in lotto:
                count += 1

        if count == 6:
            print('1등 당첨 !!!')

        elif count == 5:
            print('2등 당첨 !!!')

        elif count == 4:
            print('3등 당첨 !!!')

        elif count == 3:
            print('4등 당첨 !!!')

        else:
            print('꽝')
