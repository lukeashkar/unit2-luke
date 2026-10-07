import random
num = random.randint(1,100)
gnum = 0
used= []

while gnum != num:
    gnum= int(input("gues a number from uno to 100 - "))
    if gnum>num:
        print("yo ur number was TOO HIGH guess again lil bro")
        used.append(gnum)
        print(f"the numbers u guesed already are{used}")
    if gnum<num:
        print("ur number too tiny u gotta guess higher up")
        used.append(gnum)
        print(f"the numbers u guesed already are{used}")
    if  gnum==num:
        print("YOOOO U GOT IT UR A DEMON")