import random
game=["rock","paper","scissors"]
# print("\n"*12)
ch=int(input("Welcome to Rock Paper Scissors World :) \n\nPress '0' for Rock, '1' for Paper, '2' for Scissors : "))
r=random.randint(0,len(game)-1)
#Note: it's worth checking if the user has made a valid choice before the next line of code.
if ch>=0 and ch<=2:
    if ch==0:
        print("you chose Rock")
        print(f"Computer chose : {game[r]}")
        if game[r]=="scissors":
            print("you Won")
        else:
            print("you Lost")
    elif ch==1:
        print(f"you chose {game[1]}")
        print(f"Computer chose : {game[r]}")
        if game[r] == "rock":
            print("you Won!")
        else:
            print("you Lost")
    elif ch==2:
        print(f"you chose {game[2]}")
        print(f"Computer chose : {game[r]}")
        if game[r] == "paper":
            print("you Won!")
        else:
            print("you Lost")
else:
    print("Enter Valid Input from 0-2")

# Thank you
