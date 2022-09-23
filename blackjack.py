import random

def printcard(c):
    for i in c:
        if i // 13 == 0:
            print(chr(9824),end="")
        elif i // 13 == 1:
            print(chr(9829),end="")
        elif i // 13 == 2:
            print(chr(9830),end="")
        else:
            print(chr(9827),end="")

        if i % 13 == 0:
            print('A',end=" ")
        elif i % 13 == 10:
            print("J",end=" ")
        elif i % 13 == 11:
            print('Q',end=" ")
        elif i % 13 == 12:
            print('K',end=" ")
        else:
            print(i%13+1,end=" ")
    print()


def printmessage():
    print("玩家的牌：",end=" ")
    printcard(playercard)
    print("玩家的牌面點數：",sum(playerpoint))
    print("莊家的牌：",end=" ")
    printcard(bankercard)
    print("莊家的牌面點數：",sum(bankerpoint))
    print('---------------')

def cardpoint(x):
    if x % 13 == 0:
        return 11
    elif x % 13 > 9:
        return 10
    else:
        return x%13+1

def deal(gamercard,gamerpoint):
    temp = card.pop()
    gamercard.append(temp)
    gamerpoint.append(cardpoint(temp))

card=list(range(0,52))
random.shuffle(card)

playercard = list()
playerpoint = list()
bankercard = list()
bankerpoint = list()

for i in range(2):
    deal(playercard,playerpoint)

deal(bankercard,bankerpoint)

printmessage()

while True:
    ans = input('玩家要家牌嗎(Y/N)?')
    if ans=='N' or ans=='n':
        break
    deal(playercard,playerpoint)
    if sum(playerpoint) > 21:
        if 11 in playerpoint:
            playerpoint[playerpoint.index(11)] = 1
            printmessage()
        else:
            printmessage()
            print('完家爆牌，莊家獲勝')
            break
    else:
        printmessage()

if sum(playerpoint) < 22:
    while sum(bankerpoint) < 17:
        deal(bankercard,bankerpoint)
        if sum(bankerpoint) > 21:
            if 11 in bankerpoint:
                bankerpoint[bankerpoint.index(11)] = 1
        printmessage()

    if sum(bankerpoint) > 21 :
        print('莊家爆牌，玩家獲勝')
    elif sum(bankerpoint) > sum(playerpoint):
        print('莊家勝利')
    elif sum(bankerpoint) < sum(playerpoint):
        print('玩家獲勝')
    elif sum(bankerpoint) == sum(playerpoint):
        print('和局')