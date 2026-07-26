import random

def playSlimeRPG():

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
        choice = input('선택: ')

        if choice == '1':
            damage = random.randint(8, 15)
            monster_hp -= damage
            if damage >= 12:
                print('치명타!')
            print('슬라임에게', damage, '의 피해!')


        elif choice == '2':
            if heal > 0:
                player_hp += 10
                heal -= 1
                print('HP 10 회복!')
            else:
                print('회복약이 없습니다.')


        elif choice == '3':
            exit_game = True
            break

        else:
            print('잘못 입력!')
            continue

        if monster_hp > 0:
            monster_damage = random.randint(5, 10)
            player_hp -= monster_damage
            print('당신은', monster_damage, '의 피해를 받았습니다.')
    print()

    if exit_game:
        print('게임을 종료합니다.')
        return

    for i in range(3):
        print('.', end='')

    print()

    if player_hp > 0:
        print('승리!')
    else:
        print('패배!')