import random

def playBlackjack():
    # 카드 덱 설정하기
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # player 랑 dealer 카드 랜덤 지정
    player = []
    player.append(random.choice(cards))
    player.append(random.choice(cards))

    dealer = []
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))

    print('''========================================================
               블랙잭 게임을 시작합니다!

   딜러와 카드의 합을 비교해 21에 가장 가까운 사람이 승리합니다.
    카드의 합이 21이 넘는다면 즉시 패배하게 되니 주의하세요!!
========================================================''')

    # player 패는 보이게, 딜러 패는 하나만 공개
    print('\n플레이어: ', player)
    print('딜러: ', dealer[0], '??')

    while True:
        # 카드 팩을 더 받을지 말지 결정
        answer = input('카드를 더 받겠습니까? (y/n) : ')

        if answer == 'y':
            player.append(random.choice(cards))
            print(player)
            print('합: ', sum(player))

            if sum(player) > 21:
                print('버스트!', '패배! - 20점 차감')
                return -20

        elif answer == 'n':
            break
        else:
            print('다시 입력하세요.')

    while sum(dealer) < 17:
        dealer.append(random.choice(cards))

    # 카드 오픈, 결과 공개
    print("플레이어 :", player, sum(player))
    print("딜러 :", dealer, sum(dealer))

    if sum(dealer) > 21:
        print("딜러 버스트!", "승리! + 50점 획득")
        return 50

    elif sum(player) > sum(dealer):
        print("승리! + 50점 획득")
        return 50

    elif sum(player) < sum(dealer):
        print("패배! - 20점 차감")
        return -20

    else:
        print("무승부!")
        return 0