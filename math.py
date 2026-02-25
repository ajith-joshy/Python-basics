#Prime number
# n=int(input("Enter the number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

#fibonacci series
# l=list(map(int,input("Enter the numbers:").split()))
# for i in range(2,len(l)):
#     if l[i]!=l[i-1]+l[i-2]:
#         print(l,"Not a Fibonacci series")
#         break
# else:
#     print(l,"fibonacci series")

#factorial
# n=int(input('Enter a number:'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

#Armstrong number
# n=int(input('Enter a number:'))
# num=str(n)
# sum=0
# pow=len(num)
# for i in num:
#     sum=sum+int(i)**pow
# if sum==n:
#     print(n,"is an Armstrong number")
# else:
#     print(n,"is not an Armstrong number")

#Palindrome number
# n=int(input("Enter a number:"))
# num=str(n)
# if num==num[::-1]:
#     print(n,"is a palindrome number")
# else:
#     print(n,"is not a palindrome number")

#Sum of digits
# n=int(input('Enter a number:'))
# num=str(n)
# sum=0
# for i in num:
#     sum=sum+int(i)
# print(sum)

#LCM & GCD
# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number:"))
# gcd=1
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print("GCD:",gcd)
# lcm=(n1*n2)//gcd
# print("LCM:",lcm)

#LCM & GCD using euclidean algorithm
# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number:"))
# x=n1
# y=n2
# while n2!=0:
#     n1,n2=n2,n1%n2
# print("GCD:",n1)
# lcm=(x*y)//n1
# print("LCM:",lcm)

#leap year
# n=int(input("Enter a year:"))
# if n%400==0 or n%4==0 and n%100!=0:
#     print(n,'is a leap year')
# else:
#     print(n,'is not a leap year')

#odd or even
l=list(map(int,input("Enter the numbers:").split()))
length=len(l)
lo=[]
le=[]
for i in range(length):
    if l[i]<0:
        print(l[i],"Invalid number")
        continue
    if l[i]%2==0:
        le.append(l[i])
    else:
        lo.append(l[i])
print("Odd numbers",lo)
print("Even numbers",le)