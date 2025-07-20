import random 
print("this the game of GUESS THE NUMBER")
val= random.randint(1,101)
while True:
    target = input("what is the target or for Quit(q):: ")
    if(target == "q"):
        break
    if(int(target) == val):
        print("you won !!!")
        break
    elif(int(target) > int(val)):
        print("the number is less than you predict")
        continue
    else:
        print("the number is bigger than you predict")
        continue    
print("the game is over________!_")    