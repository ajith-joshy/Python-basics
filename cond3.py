#wap to find the max of 3 numbers
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if(a>b and a>c):
#     print(a,"is largest")
# elif(b>a and b>c):
#     print(b,"is largest")
# else:
#     print(c,"is largest")

#max of 4 numbers
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# d=int(input("Enter the fourth number:"))
# if(a>b and a>c and a>d):
#     print(a,"is largest")
# elif(b>a and b>c and b>d):
#     print(b,"is largest")
# elif(c>a and c>b and c>d):
#     print(c,"is largest")
# else:
#     print(d,"is largest")

#wap to check whether a number is 2digit,3 or 4
# n=int(input("Enter the number:"))
# if(10<=n<=99):
#     print(n,'is a 2 digit number:')
# elif(100<=n<=999):
#     print(n,'is a 3 digit number:')
# elif(1000<=n<=9999):
#     print(n,'is a 4 digit number:')
# else:
#     print("Number is either a single digit or more than four digit")

#wap to perform arithmetic operations
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# op=input("operation(+,-,*,/):")
# if(op=='+'):
#     print(n1+n2)
# elif(op=='-'):
#     print(n1-n2)
# elif(op=='*'):
#     print(n1*n2)
# elif(op=='/'):
#     print(n1/n2)
# else:
#     print("Invalid operation")

#wap to print the grade of a student
# 91<=score<=100      Grade A
# 81<=score<=90       Grade B
# 71<=score<=80       Grade C
# 61<=score<=70       Grade D
# <61                 Grade E
# score=int(input('enter the score:'))
# if(91<=score<=100):
#     print("Grade A")
# elif(81<=score<=90):
#     print("Grade B")
# elif(71<=score<=80):
#     print("Grade C")
# elif(61<=score<=70):
#     print("Grade D")
# elif(score<61):
#     print("Grade E")

#wap to check whether a triangle is equilateral, isosceles or scalene
# s1=int(input("Enter first side:"))
# s2=int(input("Enter second side:"))
# s3=int(input("Enter third side:"))
# if(s1==s2==s3):
#     print("Equilateral triangle")
# elif(s1==s2 or s2==s3 or s1==s3):
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

#wap to print number of days in a month
# name=input("Enter the month name:")
# l1=['january','march','may','july','august','october','december']
# l2=['april','june','september','november']
# l3=['february']
# if(name in l1):
#     print("31 days")
# elif(name in l2):
#     print("30 days")
# elif(name in l3):
#     print('28 or 29 days')
#using dictionary
name=input("Enter the month name:")
d={'jan':31, 'feb':28,'march':31}
if(name in d):
    print("no of days",d[name])
