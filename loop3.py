# #Given
# s="python is a programming language"
# #print each characters in the given string
# for i in s:
#     print(i,end=' ')
# print()
#
# #given a list
# l=[23,56,89,12,90,13,60]
# #print each numbers in the list
# for i in l:
#     print(i,end=" ")
# print()
#
# #Given a list
# l1=['red','green','orange','yellow','blue']
# #print each colors
# for i in l1:
#     print(i,end=" ")
# print()
#
# #Given a dictionary
# d={'country1':'India','country2':'Nepal','country3':'NewZealand','country4':'Iceland','country5':'Australia'}
# #print country names
# for i in d.values():
#     print(i,end=" ")
# print()
#
# #Given a list
# l2=['arun',34,'hello',9.8]
# #print each elements
# for i in l2:
#     print(i,end=" ")
# print()
#
# #Given
# s="python is a programming language"
# #print only the consonants in the given string
# v="aeiou"
# for i in s:
#     if i not in v and i!=" ":
#         print(i,end=' ')
# print()
#
# #given a list
# l=[23,56,89,12,90,13,60]
# #print numbers greater than 50 in the list
# for i in l:
#     if i>50:
#         print(i,end=" ")
# print()
#
# #Given a list
# l1=['red','green','orange','yellow','blue']
# #print colors whose length is less than 5
# for i in l1:
#     if len(i)<5:
#         print(i,end=" ")
# print()
#
# #Given a dictionary
# d={'country1':'India','country2':'Nepal','country3':'NewZealand','country4':'Iceland','country5':'Australia'}
# #print country names containing 'land'
# for i in d.values():
#     if 'land' in i:
#         print(i,end=" ")
# print()
#
# #Given a list
# l2=['arun',34,'hello',9.8]
# #print only the string elements
# for i in l2:
#     if type(i)==str:
#         print(i,end=" ")
# print()
#
# #series 1-10
# for i in range(1,11):
#     print(i,end=" ")
# print()
#
# #1,3,5,7,9,11
# for i in range(1,12,2):
#     print(i,end=" ")
# print()
#
# #10,20,30,....,100
# for i in range(10,101,10):
#     print(i,end=" ")
# print()
#
# #8,6,4,2,0
# for i in range(8,-1,-2):
#     print(i,end=" ")
# print()
#
# #1 4 9 16 25 36
# for i in range(1,7,):
#     print(i**2,end=" ")
# print()
#
# #10,9,8,....,-1
# for i in range(10,-2,-1):
#     print(i,end=" ")
# print()

# #-8,-6,-4,-2,0
# for i in range(-8,1,2):
#     print(i,end=" ")
# print()

# #sum of numbers in the range(1,20)
# sum=0
# for i in range(1,21,1):
#     sum+=i
# print(sum)

# #Given l=[11,34,67,23,90]
# #sum of all numbers greater than 50
# l=[11,34,67,23,90]
# sum=0
# for i in l:
#     if i>50:
#         sum+=i
# print(sum)

# #Given a dictionary
# d={'num1':46,'num2':89,'num3':60,'num4':12,'num5':67}
# #sum of numbers which are divisible by 3
# sum=0
# for i in d.values():
#     if i%3==-0:
#         sum+=i
# print(sum)

# #Given a dictionary
# d={'arun':34,'amal':56,'anu':23,'kiran':32}
# #find the average age
# sum=0
# for i in d.values():
#     sum+=i
# print("Average age is",sum/len(d))

# #factorial of a number using for loop
# n=int(input("Enter the number:"))
# fact=1
# for i in range(1,n+1):
#         fact=fact*i
# print(fact)

# #factors of a number
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#
# #multiplication table of a number
# n=int(input("Enter the number:"))
# for i in range(1,11):
#         print(i,"*",n,"=",i*n)

#sum of elements in the given list
l=[11,23,56,34]
sum=0
for i in l:
    sum=sum+i
print("sum:",sum)

#print all 3 digit numbers
for i in range(100,1000,1):
    print(i,end=" ")
print()

#given
colors=['red','green','blue','black','orange']
#print color names starting with b
for i in colors:
    if i[0]=='b':
        print(i,end=" ")
print()

#print each digits in a number
n='1234'
s=str(n)
for i in s:
    print(i,end=" ")
print()

#sum of digits in a number
n='1234'
s=str(n)
sum=0
for i in s:
    sum=sum+int(i)
print(sum)

#check whether a given number is armstrong or not
num=int(input('Enter the given number:'))
s=str(num)
pow=len(s)
sum=0
for i in s:
    sum=sum+int(i)**pow
if sum==num:
    print("Armstrong")
else:
    print("Not an Armstrong")

#reverse of a number
n=int(input("Enter the number:"))
s=str(n)
rev=""
for i in s:
    rev=i+rev
print(rev)

#reverse of a string s=hello world
s="hello world"
rev=""
for i in s:
    rev=i+rev
print(rev)