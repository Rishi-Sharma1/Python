import random

def game(comp,you):
    if comp==you:
        return None
    elif comp==1:
        if you==2:
            return True
        if you==3:
            return False
    elif comp==2:
        if you==1:
            return False
        if you==3:
            return False
    elif comp==3:
        if you==1:
            return False
        if you==2:
            return True


print("Computer's Turn : Snake(1) Water(2) or Gun(3 ) ?")
randNo=random.randint(1,3)
you=input("Player's Turn : Snake(1) Water(2) or Gun(3) ?")
print(f"Computer choose {randNo}")
print(f"You choose {you}")
a=game(randNo,you)
if a==None:
    print("Match Tied")
elif a==True:
    print("You have won the game")
else:
    print("Computer have won the game")