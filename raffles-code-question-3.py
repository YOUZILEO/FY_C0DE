import random

l2=['hotel','maker','face','clock','apple','meat','food','book','blue','green','white','mouse','phone','motor','fish','sky']

r1=random.randrange(0,len(l2))

w1=l2[r1]

r2=random.randrange(0,len(l2[r1]))
r3=random.randrange(0,len(l2[r1]))

print("The tow letters are %s & %s"%(w1[r2],w1[r3]))
print("Start guessing ~ ~ ~")

d1=input("Your answer :").lower()

i=0
while i<1000:
    i+=1
    if d1 == w1 :
        print("Congratulation your guessing is correct ! ! !")
        print("You have try %d times to find the correct answer."%(i))
        break
    if d1 != w1:
        print("Sorry, your guessing is wrong.")
        d1=input("Your answer :").lower()
    