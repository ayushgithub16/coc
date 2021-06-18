                  '''this is to check who won the game in coc'''

print("* ******** Welcome to game check of Clash of clan*********")
dp=int(input("enter destruction percentage of player 1    ANS:- "))
print(" ")
dp2=int(input("enter destruction percentage of player 2     ANS:- "))
print(" ")
th=input("is townhall destroyed by player 1?(yes/no)     ANS:-    ")
print(" ")
th2=input("is townhall destroyed by player 2?(yes/no)     ANS:-    ")
print(" ")
tim=input("enter time in minutes and seconds attacked by player 1 like:- 2 30     ANS:- ")
print(" ")
tim2=input("enter time in minutes and seconds attacked by player 2 like:- 2 30     ANS:- ")
print(" ")
if dp>50 and dp<100:
    star=int("1")
    town=(th.capitalize())
    if town=="YES":
        star=int(star)+int("1")
    else:
        star==star
elif dp<50:
    star=int("0")
    town=(th.capitalize())
    if town=="YES":
        star=int(star)+int("1")
    else:
        star==star
else:
    star=int(3)
if dp2>50 and dp2<100:
    star2=int("1")
    town=(th.capitalize())
    if town=="YES":
        star2=int(star2)+int("1")
    else:
        star2==star2
elif dp2<50:
    star2=int("0")
    town=(th.capitalize())
    if town=="YES":
        star2=int(star2)+int("1")
    else:
        star2==star2
else:
    star2=int(3)

if int(star)>int(star2):
    print("Player 1 won the game")
elif int(star)<int(star2):
    print("Player 2 won the game")
else:
    if int(dp)>int(dp2):
        print("Player 1 won the game")
    elif int(dp)<int(dp2):
        print("Player 2 won the game")
    else:
        min=tim[0:1]
        sec=tim[2:]
        min2=tim2[0:1]
        sec2=tim2[2:]
        if int(min)>int(min2):
            print("Player 2 won the game")
        elif int(min)<int(min2):
            print("Player 1 won the game")
        else:
            if int(sec)>int(sec2):
                print("Player 2 won the game")
            else:
                print("Player 1 won the game")



                

        


