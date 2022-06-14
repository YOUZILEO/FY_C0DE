print("Input your mark and you will get your grade.")

m1=int(input("Please input your question 1 mark: "))
m2=int(input("Please input your question 2 mark: "))
m3=int(input("Please input your question 3 mark: "))
m4=int(input("Please input your question 4 mark: "))
m5=int(input("Please input your question 5 mark: "))

def grade_function(mark):
    if 89<mark<101:
        return 'A'
    elif 79<mark<90:
        return 'B'
    elif 69<mark<80:
        return 'c'
    elif 59<mark<70:
        return 'D'
    elif mark<60:
        return 'F'

print("The grade of question 1 is",grade_function(m1))
print("The grade of question 2 is",grade_function(m2))
print("The grade of question 3 is",grade_function(m3))
print("The grade of question 4 is",grade_function(m4))
print("The grade of question 5 is",grade_function(m5))