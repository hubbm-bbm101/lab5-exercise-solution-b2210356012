import random
number=random.randint(1,100)
guess=None
while guess!=number:
    guess=int(input("Do you feel lucky today? Make a guess!"))
    if guess>number:
        print("Too high decrease it please!")
    elif guess<number: 
        print("Nope,try to increase next time")
print("Well done! I knew you were lucky")