import random

def playBlackjack():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

    print('\n플레이어: ', player)
    print('딜러: ', dealer[0], '??')

    while True:
        answer = input('카드를 더 받겠습니까? (y/n) : ')

        if answer == 'y':
            player.append(random.choice(cards))
            print(player)
            print('합: ', sum(player))

            if sum(player) > 21:
                print('버스트!', '패배!')
                return

        elif answer == 'n':
            break
        else:
            print('다시 입력하세요.')

    while sum(dealer) < 17:
        dealer.append(random.choice(cards))

    print("플레이어 :", player, sum(player))
    print("딜러 :", dealer, sum(dealer))

    if sum(dealer) > 21:
        print("딜러 버스트!", "승리!")

    elif sum(player) > sum(dealer):
        print("승리!")

    elif sum(player) < sum(dealer):
        print("패배!")

    else:
        print("무승부!")