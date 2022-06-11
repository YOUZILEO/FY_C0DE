#s1={1,2,3,4,1,2,23,34,4,5}
#s2={3333333,3,33,3,3,3,8,4848,4,4,46,66,56,6,564515,15,61,5,1,12,12,12,1,269,89,4,94,9,97,9,978,23,23,3,3,3,33,3,}
#s3=s1^s2
#print(s3)
#s=set("lieuyanyu")
#print(s)
#dic={"apple":"苹果","bug":"错误"}
#print(dic["apple"])
#print("apple" not in dic)
#del dic["apple"]
#print(dic)
#dic={x:x*2 for x in [2,3,4]}
#print(dic)
#s1=set("hello")
#print(s1)
#x=input("请输入数字：")
#x=int(x)
#if x>200:
    #print("大于200")
#elif x>100:
    #print("小于200，大于100")
#else:
    #print("未知")
#n1=int(input("请输入第一个数字："))
#n2=int(input("请输入第二个数字："))
#op=input("请输入运算：+，-，*，/")
#if op=="+":
    #print(n1+n2)
#elif op=="-":
    #print(n1-n2)
#elif op=="*":
    #print(n1*n2)
#elif op=="/":
    #print(n1/n2)
#else:
    #print("格式错误")
#n1=int(input("请输入第一个数字："))
#n2=int(input("请输入第二个数字："))
#n3=input("请选择运算:+,-,*,/,**")
#if n3=="+":
 #   print(n1+n2)
#elif n3=="-":
 #   print(n1-n2)
#elif n3=="*":
 #   print(n1*n2)
#elif n3=="/":
 #   print(n1/n2)
#elif n3=="**":
 #   print(n1**n2)
#else :
 #   print("笨蛋")
#x=1
#sum=0
#while x<=9:
 #   sum=sum+x
 #   x+=1
#print(sum)
#sum=0
#for x in range(1,11):
#    sum=sum+x
#print(sum)
#n=1
#while n<5:
#    if  print(n)
#    n+=1
#print("最终的n:",n)
#n=0
#for x in {0,1,2,3}:
#    if x%2==0:
#        continue
#    print(x)
#    n+=1
#print(n)
#sum=0
#for n in range(11):
#    sum+=n
#else:
#    print(sum)
#x=input("请输入数字：")
#x=int(x)
#for i in range(x):
#    if i*i==x:
#        print("整数平方根",i)
#        break
#else:
#    print("没有此数字的平方根")
#def s1(x,y):
#    print(x*y)
#    return x*y
#s1(9,99)
#z=s1(9,9)+s1(7,7)
# #print(z)
# def c(z):
#    sum=0
#    for n in range(1,z+1):
#        sum=sum+n
#    print(sum)
#c(10)
#c(20)
# import random
# benjin=300
# money=50
# duzhu=10
# print("欢迎来到骰子游戏")
# while True :
#     print("目前的的金额：",benjin)
#     print("每局赌注：",duzhu)
#     x=[]
#     for i in range(3):
#         y=random.choice([1,2,3,4,5,6])
#         x.append(y)
#     print(x)
#     print("请预测本局的三颗骰子的个别数值")
#     a1=int(input("第一个数值："))
#     a2=int(input("第二个数值："))
#     a3=int(input("第三个数值："))
#     if a1 in x:
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a2 in x:
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a3 in x :
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a1 and a2 in x:
#         print("恭喜猜中其中两个值,获得福利10元")
#         benjin+=10
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a1 and a2 in x:
#         print("恭喜猜中其中两个值,获得福利10元")
#         benjin+=10
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a2 and a3 in x:
#         print("恭喜猜中其中两个值,获得福利10元")
#         benjin+=10
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a1 and a1 and a3 in x:
#         print("恭喜猜中其中三个值,获得福利20元")
#         benjin+=20
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if benjin==0:
#         print("目前的的金额：",benjin)
#         print("你已耗尽全部金额，如想继续，请前往贷款部接洽")
#         break
#     if benjin<0:
#         print("目前的的金额：",benjin)
#         print("你已耗尽全部金额，并且倒欠本会",benjin)
#         print("请在一个星期内还清，否则本会将让你体验十八层地狱")
#         break
#     usernum=input("若要退出，请输入Q/q ；若想继续，则输入任意字母：")
#     if usernum=="Q"or usernum=="q":
#         break