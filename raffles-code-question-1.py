l1=[]
i=0

print("Input any number to the list , then it will show the second largest number in the list.")

d1=int(input("Please input your list data: "))
d2=input("Do you want to continue input or stop input ? \n Continue == C/c      Stop == S/s\n")

while i<1000:
    i+=1
    l1.append(d1)
    d1=int(input("Please input your list data: "))
    d2=input("Do you want to continue input or stop input ? \n Continue == C/c      Stop == S/s\n")
    if d2 == 'S'or d2 =='s':
        l1.append(d1)
        break

print("Your list is \n",l1)
l1.sort()
print("After sorted\n",l1)
print("The second largest number in the list is ",l1[-2])
