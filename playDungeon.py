import random
def playDungeon():
    hp = 100
    gold = 0
    round = 1

    print('던전 게임을 시작합니다.')
    print('10번째 칸에 도착하면 승리!  |  체력이 0이 되면 패배합니다.')

    while hp > 0 and round < 10:
        input('\n엔터를 눌러 앞으로 이동')
        event = random.choice(['몬스터', '보물', '회복', '함정'])
        print(f'\n현재 {round}칸에 도착했습니다.')
        round += 1

        if event == '몬스터':
            print('몬스터 등장!')

            while True:
                answer = input('공격 하시겠습니까? y/n :')
                damage = random.randint(20, 40)
                if answer == 'y':
                    success = random.randint(1, 100)
                    if success <= 50:
                        print('공격 성공! 아무 피해 없이 다음 칸으로 이동합니다 !')

                    else:
                        print(f'공격 실패! {damage}의 피해를 입고 뒤로 돌아갑니다.')
                        round -= 2
                    break

                elif answer == 'n':
                    print(f'비겁합니다! {damage}의 피해를 입었습니다.')
                    break

                else:
                    print('잘못입력했습니다.')


                hp -= damage

        elif event == '보물':
            print('보물을 찾았습니다!')
            gain_gold = random.randint(10, 50)
            gold += gain_gold
            print(f'++++++ {gain_gold} 골드를 얻었습니다.')

        elif event == '회복':
            print('회복 포션 발견!!')
            hp += 10

        elif event == '함정':
            print('함정을 밟았습니다!')
            print('30의 피해를 입고, 뒤로 한 칸 물러납니다.')
            hp -= 30
            gold -=20
            round -= 2


        print(f'''=====================
   현재 체력 : {hp}
   현재 골드 : {gold}
=====================''')
    if round ==10:
        print('승리!', '도착지에 도착했습니다.')
    elif hp < 0:
        print('패배!', '체력을 모두 잃었습니다.')