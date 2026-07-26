import random

def playLotto():
    # 1-45까지 수 중 랜덤 6개 지정
    lotto = random.sample(range(1, 46), 6)
    score = 0

    print('로또를 구매합니다. 1부터 45까지 숫자 중 6개를 입력하시오.')

    while True:

        # 유저 입력값 정의
        user = list(map(int, input('''예시) 1 20 43 7 9 15  
:''').split()))

        # 잘못 입력시 재입력 요구
        if len(user) != 6:
            print('숫자 6개를 입력하세요.')
            continue

        # 유저 입력 값이 랜덤 로또 번호와 얼마나 일치하는가 판단
        count = 0

        for num in user:
            if num in lotto:
                count += 1

        if count == 6:
            print('1등 당첨 !!! + 500점 획득')
            score = 500


        elif count == 5:
            print('2등 당첨 !!! + 200점 획득')
            score = 200


        elif count == 4:
            print('3등 당첨 !!! + 80점 획득')
            score = 80


        elif count == 3:
            print('4등 당첨 !!! + 20점 획득')
            score = 20


        else:
            print('꽝 + 0점 획득')
            score = 0
            break

    # 결과 도출
    return score