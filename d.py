# import makefood
# print("这是第一题\n")
# print("欢迎来到幸平面馆")
# noodle=input("请输入想食用的面类：")
# peiliaos=input("请输入想要的配料：")
# makefood.noodles(noodle,peiliaos)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("这是第二题\n")
# import random
# min,max=1,50
# winpercent=30
# last=[1]
# while True :
#     print("猜大小游戏，B/b表示大，S/s表示小，Q/q表示结束")
#     usernum=input("=")
#     if usernum=="Q"or usernum=="q":
#         break
#     num=random.randint(min,max)
#     if num>=winpercent:
#         print("恭喜你猜对了")
#         print("共尝试了",next,"次")
#     else:
#         print("猜错了，请再猜多一次")
#         next=last[0]+1
#         last[0]=next
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("这是第三题\n")
# import jisuan
# print("欢迎使用基本运算")
# x=int(input("请选择运算模式（1=加法，2=减法，3=乘法，4=除法）:"))
# if x==1:
#     jisuan.jiafa()
# elif x==2:
#     jisuan.jianfa()
# elif x==3:
#     jisuan.chenfa()
# elif x==4:
#     jisuan.chufa()
# else :
#     print("无效输入")
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("这是第四题\n")
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
#     A1=input("请预测本局骰子数总和会不会大于9(若总和为9，即庄家获胜)：")
#     A2=int(input("请预测本局骰子数的总和："))
#     print("请预测本局的三颗骰子的个别数值")
#     a1=int(input("第一个数值："))
#     a2=int(input("第二个数值："))
#     a3=int(input("第三个数值："))
#     T1=sum(x)
#     if A1=="会" or "hui":
#         e=1
#     else:
#         e=0
#     if T1>9:
#         f=1
#     elif T1<9:
#         f=0
#     else:
#         f=2
#     if e==f:
#         print("恭喜你答对第一项")
#         benjin+=money
#         benjin-=duzhu
#     else:
#         print("抱歉，你答错第一项")
#         benjin-=money
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if A2==T1:
#         print("恭喜你答对第二项")
#         benjin+=money
#         benjin-=duzhu
#     else:
#         print("抱歉，你答错第二项")
#         benjin-=money
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     print("欢迎来到第三项")
#     if a1 in x:
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         print("抱歉你没猜中其中的值")
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a2 in x:
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         print("抱歉你没猜中其中的值")
#         benjin-=duzhu
#     print("目前的的金额：",benjin)
#     if a3 in x :
#         print("恭喜答对其中一个值")
#         benjin+=20
#         benjin-=duzhu
#     else:
#         print("抱歉你没猜中其中的值")
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
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("这是第五题\n")
# y=[]
# for x in input("请输入五个字母的英文字："):
#     y.append(x)
# print(y)
# while True:
#     if y==[]:
#         break
#     y.pop()
#     print(y)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("这是第六题\n")
# import random
# x=random.sample(range(1,48),8)
# z=x.pop()
# print("本期的特别号码：",z)
# y=sorted(x)
# print("本期的7个一般号码：",y)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# x=(input("请输入第一位元："))
# y=(input("请输入第二位元："))
# def chufa():#除法
#     try:
#         a=(int(x))/(int(y))
#     except Exception:
#         print("资料输入错误")
#     else:
#         print(a)
# chufa()
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             for d in range(0,10):
#                 for e in range(0,10):
#                     x=[a,b,c,d,e]
#                     y=x.copy()
#                     y.sort()
#                     z=list(set(y))
#                     if y==z:
#                         for v in y:
#                             if (a*10000+b*1000+c*100+d*10+e)*a==e*111111:
#                                 print("(",a,b,c,d,e,")*",a,"=",e*111111)
#                                 break
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# showDebug=int(input("要查看最新的六合彩号码排序过程吗？【1】要；【2】嫑："))
# def bubbleSort(x):
#     s=1
#     for i in range(len(x)-1):
#         print()
#         if s==1:
#             s=0
#             for j in range(len(x)-1-i):
#                 if x[j]<x[j+1]:
#                     x[j],x[j+1]=x[j+1],x[j]
#                     s=1
#             if showDebug==1:
#                 print("第",i+1,"轮",x)
#         else:
#             break
#     return x
# def numMaker(a,b,n):
#     import random
#     y=random.sample(range(a,b),n)
#     return y
# z=numMaker(0,42,6)
# print("六合彩号码：",z)
# print("排序后的结果：",bubbleSort(z))
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# def Sort(A):
#     for i in range(len(A)):
#             min = i
#             for j in range(i+1,len(A)):
#                 if A[min]>A[j]:
#                     min=j
#             A[i],A[min]=A[min],A[i]
#     return A
# A=[6988,6982,6658,6045,6387,7654,7097,8868,9180,9353,9105,8574,11079,11618,13215,12541,12528,10710]
# print("排序前的病例：",A)
# print("排序后的病例：",Sort(A))
# print("病例数最高值：",max(A))
# print("病例数最低值：",min(A))
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
#import shuru
# shuru.shuru()
# while(True):
#     cq=input("是否退出？\n退出Q/q 不退出C/c \n")
#     if (cq=="C"or cq=="c"):
#         shuru.shuru()
#     elif (cq=="Q"or cq=="q"):
#         case=shuru.read()
#         shuru.Sort(case)
#         print("病例最小值：",case[-1])
#         print("大到小排列：\n",case)
#         break
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# import shuru
# import random
# shuru.name()
# while(True):
#     cs=input("是否退出？\n退出S/s 不退出C/c \n")
#     if (cs=="C"or cs=="c"):
#         shuru.name()
#     elif (cs=="S"or cs=="s"):
#         name=shuru.read_name()
#         print("随机输出名字：",random.choice(name))
#         break
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# b=8
# for c in a :
#     d=c%b
#     d-=1
#     print(d)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")

