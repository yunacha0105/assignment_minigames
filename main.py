from playBlackjack import playBlackjack
from playDungeon import playDungeon
from playSlimeRPG import playSlimeRPG
from playLotto import playLotto
from playRSP import playRSP
from playUpdown import playUpdown

# 메뉴출력
print('''====================
      게임 목록
====================

1. 업다운 게임
2. 가위바위보 게임
3. 로또 번호 출력
4. 슬라임 RPG
5. 던전 탐험 게임
6. 블랙잭 21 게임
7. 나가기
''')

while True:
    #메뉴 입력 받기
    menu = int(input('''플레이하고 싶은 게임의 메뉴를 입력하세요.
    : '''))

    if menu == 1:
        playUpdown()
    elif menu == 2:
        playRSP()
    elif menu == 3:
        playLotto()
    elif menu == 4:
        playSlimeRPG()
    elif menu == 5:
        playDungeon()
    elif menu == 6:
        playBlackjack()
    elif menu == 7:
        break
    else:
        print('잘못입력하셨습니다.')
        continue