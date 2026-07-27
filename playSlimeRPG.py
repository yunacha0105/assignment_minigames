import random

def playSlimeRPG():

    # 변수 설정
    player_hp = 50
    monster_hp = 40
    heal = 2
    exit_game = False

    print('======== 슬라임 RPG ========')

    while player_hp > 0 and monster_hp > 0:

        print(f'''--------------------------- 
        내 HP: {player_hp}
     슬라임 HP: {monster_hp}
        1.공격
        2.회복
        3.종료
-------------------------- ''')
        # 사용자 입력값 설정
        choice = input('선택: ')

        # 공격
        if choice == '1':
            damage = random.randint(8, 15)
            monster_hp -= damage
            if damage >= 12:
                print('치명타!')
            print('슬라임에게', damage, '의 피해!')

        # 회복
        elif choice == '2':
            if heal > 0:
                player_hp += 10
                heal -= 1
                print('HP 10 회복!')
            else:
                print('회복약이 없습니다.')

        # 종료
        elif choice == '3':
            exit_game = True
            break

        else:
            print('잘못 입력!')
            continue

        # 슬라임 매 차례마다 공격값 정의
        if monster_hp > 0:
            monster_damage = random.randint(5, 10)
            player_hp -= monster_damage
            print('당신은', monster_damage, '의 피해를 받았습니다.')
    print()

    # 게임 종료
    if exit_game:
        print('게임을 종료합니다.')
        return 0

    # 구분선 입력
    for i in range(3):
        print('.', end='')

    print()

    # 결과 도출
    if player_hp > 0:
        print('승리! + 50점 획득')
        return 50

    else:
        print('패배! - 20점 차감')
        return -20