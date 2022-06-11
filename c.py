# print("第一题\n")
# name=("小黄","小明","小王","老王","小月")
# print("复仇者小队") 
# for x in name :
#     print(x)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第二题\n")
# name=("小黄","小明","小王","老王","小月","大黄","大明","大月")
# print("新的复仇者小队")
# for x in name :
#     print(x)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第三题\n")
# tp=("1","2","3","4","5","2","3","1","4")
# x=set(tp)
# y=list(x)
# y.sort()
# newtp=tuple(y)
# for z in newtp:
#     print(z)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第四题\n")
# h=(30,28,29,28,31,29,33)
# d=(26,27,26,26,30,25,30)
# print("一周最高温",max(h))
# print("一周最低温",min(d))
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
#第九章
# print("第一题\n")
# day={"MONDAY":"星期一","TUESDAY":"星期二","WEDNESDAY":"星期三","THURSDAY":"星期四","FRIDAY":"星期五","SATURDAY":"星期六","SUNDAY":"星期天"}
# x=input("请输入星期几：")
# z=x.upper()
# if z in day.keys():
#     print("%s的华文是%s"%(z,day[z]))
# else:
#     print("输入错误")
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第二题\n")
# month={"一月":"JANUARY","二月":"FEBRUARY","三月":"MARCH","四月":"APRIL","五月":"MAY","六月":"JUNE","七月":"JULY","八月":"OGOS","九月":"SEPTEMBER","十月":"OCTOBER","十一月":"NOVEMBER","十二月":"DECEMBER"}
# x=input("请输入月份：")
# if x in month.keys():
#     print("%s的英文是%s"%(x,month[x]))
# else:
#     print("输入错误")
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第三题\n")
# fruits={"Watermelon":"15","Banana":"20","Pineapple":"25","Orange":"12","Apple":"18"}
# print(fruits)
# x=sorted(fruits.items())
# print(x)
#第十章
# print("第一题\n")
# w=[]
# z=[]
# for x in range(0,100,3):
#     w.append(x)
#     a=set(w)
# for y in range(0,101,5):
#     z.append(y)
#     b=set(z)
# print("A串联：",a)
# print("B串列：",b)
# print("\n")
# print("A与B的交集：",a&b)
# print("\n")
# print("A与B的连集：",a|b)
# print("\n")
# print("A-B的差集：",a-b)
# print("\n")
# print("B-A的差集：",b-a)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# print("第二题\n")
# Math={"A","B","C","D","E","G","H","I"}
# Compute={"B","D","G","W","X","Y","Z"}
# Physics={"B","C","L","X","Z"}
# print("同时参加三个生活营的名单：",Math&Compute&Physics)
# print("\n")
# print("同时参加Math和Computer生活营的名单:",Math&Compute)
# print("\n")
# print("同时参加Math和Physics生活营的名单:",Math&Physics)
# print("\n")
# print("同时参加Computer和Physics生活营的名单:",Compute&Physics)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# accounts=[]
# passwords=[]
# account=input("请创建账号：")
# print(account)
# password=input("请创建密码：")
# print(password)
# accounts.append (account)
# passwords.append(password)
# print("欢迎来到云之国")
# ac=input("请输入账号：")
# print(ac)
# ps=input("请输入密码：")
# print(ps)
# if ac in accounts and ps in passwords:
#     print("Welcome")
# else:
#     print("Error")
# def onepice(a,b="罗"):
# print("我喜欢的人物是"+a)
# print("我最喜欢的人物是"+a+"和"+b)
# print()
# onepice("路飞")
# onepice("娜美","罗宾")
# # print("\n————————————————————————————————我是分割线————————————————————————————————\n")def jsj(x,y):
#     jia=x+y
#     jian=x-y
#     chen=x*y
#     chu=x/y
#     return jia,jian,chen,chu
# x=int(input("请输入X值："))
# y=int(input("请输入Y值："))
# jia,jian,chen,chu=jsj(x,y)
# print("x+y=",jia)
# print("x-y=",jian)
# print("x*y=",chen)
# print("x/y=",chu)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n"）
# def ljxx(gks):
#     y="敬爱的"
#     e="本动漫将于X月X日发布"
#     s="敬请关注"
#     for gk in gks:
#         xx=y+gk+"\n"+e+"\n"+s+"\n"
#         print(xx)
# md=["A","B","C"]
# ljxx(md)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n"）
# def Gequ(geci):
#     for fh in geci:
#         if fh in ".-',":
#             geci=geci.replace(fh," ")
#         return geci
# def ziyuanjisuan(gecijisuan):
#     gequlist=gecijisuan.split()
#     print("以下是歌词串列")
#     for zyjs in gequlist:
#         if zyjs in dict:
#             dict[zyjs]+=1
#         else:
#             dict[zyjs]=1
# geci="""Hey, I was doing just fine before I met you
# I drink too much, and that's an issue, but I'm okay
# Hey, you tell your friends it was nice to meet them
# But I hope I never see them again
# I know it breaks your heart
# Moved to the city in a broke-down car, and
# Four years, no calls
# Now you're looking pretty in a hotel bar, and
# I-I-I can't stop
# No, I-I-I can't stop
# So, baby, pull me closer
# In the back seat of your Rover
# That I know you can't afford
# Bite that tattoo on your shoulder
# Pull the sheets right off the corner
# Of that mattress that you stole
# From your roommate back in Boulder
# We ain't ever getting older
# We ain't ever getting older
# We ain't ever getting older
# You look as good as the day I met you
# I forget just why I left you, I was insane 
# Stay and play that…"""
# dict={}
# print("将歌词转换小写并去除标点符号且用字元取代")
# gequ=Gequ(geci.lower())
# print(gequ)
# ziyuanjisuan(gequ)
# print("结果")
# print(dict)
# print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# shuzhi=int(input("请输入数值："))
# def jueduizhi(shuzhi):
#     if shuzhi<=0:
#         shuzhi*=(-1)
#         print("其绝对值：",shuzhi)
#     else:
#         print("其绝对值为：",shuzhi)
# jueduizhi(shuzhi)
#print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# def jixu():
#     a=input("若想继续请输入y，否则任意输入任何字符即可结束")
#     if a=="y":
#         jisuan()
# def jisuan():
#     x=int(input("请输入数值1："))
#     y=int(input("请输入数值2："))
#     z=input("请选择计算方式：")
#     if z=="+":
#         a=x+y
#         print("结果是",a)
#     elif z=="-":
#         a=x-y
#         print("结果是",a)
#     elif z=="*":
#         a=x*y
#         print("结果是",a)
#     else:
#         z=="/"
#         a=x/y
#         print("结果是",a)
#     jixu()
# jisuan()
#print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# def pizza(chicun,kowei,*peiliaos):
#     print("您所选的PIZZA尺寸是",chicun,"寸，口味是",kowei)
#     print("配料如下：")
#     for peiliao in peiliaos:
#         print(peiliao)
# pizza("7","夏威夷","黄莉","虾仁","cheese","灯笼椒","火腿")
#print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# import Frist
# Frist.c(1)
# import jisuan
# jisuan.chufa()
# import random
# min,max=1,100
# winpercent=int(input("专家获胜的几率（0~100）："))
# while True :
#     print("猜大小游戏，B/b表示大，S/s表示小，Q/q表示结束")
#     usernum=input("=")
#     if usernum=="Q"or usernum=="q":
#         break
#     num=random.randint(min,max)
#     if num>=winpercent:
#         print("恭喜你猜对了")
#     else:
#         print("猜错了，请再猜多一次")
# import time
# xtime=time.localtime()
# print(xtime)
# import calendar
# print(calendar.calendar(2020))
#print("\n————————————————————————————————我是分割线————————————————————————————————\n")
# import Frist
# import random
# benjin=300
# money=100
# duzhu=50
# min,max=1,100
# winpercent=int(input("庄家获胜的几率（0~100）："))
# while True :
#     print("目前的的金额：",benjin)
#     print("每局赌注：",duzhu)
#     print("猜大小游戏，B/b表示大，S/s表示小，Q/q表示结束")
#     usernum=input("=")
#     if usernum=="Q"or usernum=="q":
#         break
#     num=random.randint(min,max)
#     if num>winpercent:
#         print("恭喜你猜对了")
#         benjin+=money
#         benjin-=duzhu
#     else:
#         print("猜错了，请再猜多一次")
#         benjin-=money
#         benjin-=duzhu
#     if benjin==0:
#         print("目前的的金额：",benjin)
#         print("你已耗尽全部金额，如想继续，请前往贷款部接洽")
#         break
#     if benjin<0:
#         print("目前的的金额：",benjin)
#         print("你已耗尽全部金额，并且倒欠本会",benjin)
#         print("请在一个星期内还清，否则本会将让你体验十八层地狱")
#         break