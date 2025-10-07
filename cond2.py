#wap to check whether a number is 3 digit or not
# num=int(input("Enter a number:"))
# if(100>=num<=999):
#     print(num,"is a 3 digit number")
# else:
#     print(num,"is not a 3 digit number")

#wap to check whether the last number entered is a multiple of 3 or not
# num=int(input("Enter a number:"))
# last_digit=num%10
# if(last_digit%3==0):
#     print("Last number is a multiple of 3")
# else:
#     print("Last number is not a multiple of 3")

#wap to check whether the entered character is a vowel or not
# chr=input("Enter the character:")
# v="aeiouAEIOU"
# if(chr in v):
#     print(chr,"is a vowel")
# else:
#     print(chr,"is not a vowel")

#wap to check whether the entered number is in the list or not
# l=[23,56,89,12,80]
# num=int(input("Enter a number:"))
# if(num in l):
#     print(num,"is in list")
# else:
#     print(num,"not in list")

#wap to check whether the entered name is in the dictionary or not
# d={'name':'arun','age':25,'place':'ekm'}
# name=input("Enter a name:")
# if(name in d.values()):
#     print(name,"is in the dictionary")
# else:
#     print(name,'is not in dictionary')

#wap to check whether the two entered strings are equal or not
# x=(input("Enter the first string:"))
# y=(input("Enter the second string:"))
# if(x==y):
#     print("Both are equal")
# else:
#     print("They are not equal")

#wap to check whether the palindrome of string is equal or not
# str=input("Enter the string:")
# if(str[::-1]==str):
#     print(str,"is a palindrome")
# else:
#     print(str,"is not a palindrome")

#wap to check the maximum of two numbers
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if(x>y):
    print(x,"is greater than",y)
else:
    print(y,"is greater than",x)