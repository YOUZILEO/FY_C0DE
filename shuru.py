# def shuru():
#     shuru=open("shuru.txt",mode='a')
#     case=input("请输入今天的病例：")
#     shuru.write(case)
#     shuru.write('\n')
#     shuru.close


# def read():
#     with open("shuru.txt") as filename:
#         data=filename.readlines()
#         return data


# def Sort(case):
#     for i in range(len(case)):
#             min = i
#             for j in range(i+1,len(case)):
#                 if case[min]<case[j]:
#                     min=j
#             case[i],case[min]=case[min],case[i]
#     return case

# def name():
#     name=open("name.txt",mode='a',encoding='utf-8')
#     nama=input("请输入名字：")
#     name.write(nama)
#     name.write('\n')
#     name.close

# def read_name():
#     with open("name.txt",encoding='utf-8')as fn:
#         mingzi=fn.readlines()
#         return mingzi
