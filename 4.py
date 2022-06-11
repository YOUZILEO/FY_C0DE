# #请预测本局骰子数总和会不会大于9(若总和为9，即庄家获胜) ✔
# #请预测本局骰子数的总和 ✔
# #请预测本局的三颗骰子的个别数值 ✔
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
#     if a1 and a1 and a3 in x:
#         print("恭喜猜中全部三个值,获得福利50元")
#         benjin+=money
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



















































