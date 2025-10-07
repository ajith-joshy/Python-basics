#addition of two numbers
# def add():
#     "Addition of two numbers"
#     n1=int(input("Enter number:"))
#     n2=int(input("Enter number:"))
#     s=n1+n2
#     print(s)
#     return
# add()

# #Define the function to find the factorial of a number
# def fact():
#     "Factorial of a number"
#     n=int(input("Enter the number:"))
#     fact=1
#     for i in range(1,n+1):
#          fact=fact*i
#     print(fact)
#     return
# fact()

#define a function to find the reverse of a number
# def rev():
#     n=int(input("Enter number:"))
#     s=str(n)
#     print(s[::-1])
#     return
# rev()

#define a function to check whether a number is prime or not
# def prime():
#     n=int(input("Enter the number:"))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#                 print(n,"not a prime number")
#         else:
#             print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")
#     return
# prime()

#define a function to find the BMI value
#bmi=weight/height**2
# def BMI():
#     weight=int(input("Enter weight:"))
#     height=int(input("Enter height:"))
#     bmi=weight/height**2
#     print("BMI is",bmi)
#     return
# BMI()

#define an addition function without using parameters
# def add(n1,n2):
#     s=n1+n2
#     print(s)
#     return
# #add(30,67)
# a=int(input("Enter number:"))
# b=int(input("Enter number:"))
# add(a,b)

#write a function to find the simple interest using parameters and arguments
# def interest(p,n,r):
#     interest=p*n*r/100
#     print(interest)
#     return
# p=int(input("Enter the principle amount:"))
# n=int(input("Enter number of years:"))
# r=int(input("Enter interest rate:"))
# interest(p,n,r)

#Define a function to find the count of a specific character in a string using parameters and arguments
# def count(s,ch):
#     c=0
#     for i in s:
#         if i==ch:
#             c=c+1
#     print(c)
# s=input("Enter the word:")
# ch=input("Enter the character:")
# count(s,ch)

#using return(sum)
# def add(n1,n2):
#     s=n1+n2
#     return s
# s=add(7,8)
# print(s)

#define a function to find the area of a circle(using return)
# def area(r):
#     area=3.14*r**2
#     return area
# a=area(4)
# print(a)

#define a function to check whether a number is armstrong number
#return true if number is armstrong else return false
def armstrong(n):
    sum=0
    s=str(n)
    digit=len(s)
    for i in s:
        sum=sum+int(i)**digit
    if sum==n:
        return True
    else:
        return False
arm=armstrong(123)
print(arm)
