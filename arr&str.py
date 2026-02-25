# reverse
# array/list
# list=list(map(int,input("Enter the numbers:").split()))
# print(list[::-1])

# string
# s=input('Enter a string:')
# print("Reverse of the string is ",s[::-1])

# print unique elements
# array/list
# l1=list(map(int,input("Enter the numbers:").split()))
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

#string
# s=input("Enter a string:")
# s2=" "
# for i in s:
#     if i not in s2:
#         s2+=i
# print(s2)

#find duplicates
#array/list
# l=list(map(int,input("Enter the numbers:").split()))
# l1=[]
# for i in l:
#     if l.count(i)>1 and i not in l1:
#         l1.append(i)
# print(l1)

#string
# s=int(input('enter a string'))
# s1=str(s)
# s2=" "
# count=0
# for i in s1:
#     if s1.count(i)>1 and i not in s2:
#         s2=s2+i
# print(s2)

#rotate array
#right by 2 positions
# a=list(map(int,input("Enter the numbers:").split()))
# k=2
# a=a[-2:]+a[:-2]
# print(a)
#left by 2 positions
# a=list(map(int,input("Enter the numbers:").split()))
# k=2
# a=a[2:]+a[:2]
# print(a)

#second largest
# l=list(map(int,input("Enter the numbers:").split()))
# l.sort()
# print(l[-2])

#second smallest
# l=list(map(int,input("Enter the numbers:").split()))
# l.sort()
# print(l[1])

#string palindrome
# s=input("Enter a string:")
# s1=s[::-1]
# if s==s1:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")

#count vowels
# s=input("Enter a string:")
# v="aeiouAEIOU"
# count=0
# for i in s:
#     if i in v:
#         count=count+1
# print(count)

#frequency of characters
# s=input('Enter a string:')
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)

#remove spaces
# s=input("Enter:")
# s1=""
# for i in s:
#     if i!=" ":
#         s1=s1+i
# print(s1)

#special characters
# s=input('Enter:')
# sc="/?!@#$%^&*()"
# s1=""
# for i in s:
#     if i in sc:
#         continue
#     else:
#         s1=s1+i
# print(s1)

#anagram check
# s1=input("Enter a string:").lower()
# s2=input("Enter a string:").lower()
# if sorted(s1)==sorted(s2):
#     print('Anagram')
# else:
#     print('Not Anagram')

#check if array is sorted
# def check(l):
#     n=len(l)
#     for i in range(n-1):
#         if l[i]>l[i+1]:
#             print(l,"is not sorted")
#             break
#     else:
#         print(l,"is sorted")
# l=list(map(int,input("Enter the numbers:").split()))
# check(l)

#merge two arrays
# def merge(l1,l2):
#     for i in l2:
#         l1.append(i)
#     print(l1)
# merge([1,2,3],[4,5,6])

#character frequency
# s=input("Enter a string:")
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)

#first non-repeating character
# s=input("Enter a string:")
# for i in s:
#     if s.count(i)<2:
#         print(i)
#         break

#Stack
# stack=[]
# while True:
#     print("1.Push")
#     print("2.Pop")
#     print("3.Peek")
#     print("4.Display")
#     print("5.Reverse")
#     print("6.Exit")
#
#     n=int(input("Enter your choice:"))
#     if n==1:
#         item=int(input("Enter the element to be pushed:"))
#         stack.append(item)
#         print("Pushed")
#     elif n==2:
#         stack.pop()
#         print("Popped")
#     elif n==3:
#         top=stack[-1]
#         print("Top element:",top)
#     elif n==4:
#         print(stack)
#     elif n==5:
#         rev=stack[::-1]
#         print("Reversed stack:",rev)
#     else:
#         print("Invalid input")

#Reverse string using stack
# s=input("Enter a string:")
# stack=[]
# for i in s:
#     stack.append(i)
# rev=""
# while stack:
#     rev=rev+stack.pop()
# print(rev)

#IBM Coding question
#same then new subsequence, different then same subsequence
# def getMinSubsequences(s):
#     max_count=1
#     current_count=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             current_count+=1
#             max_count=max(max_count,current_count)
#         else:
#             current_count=1
#     print(max_count)
# getMinSubsequences("100011")

#different then new subsequence, same then same subsequence
# def countsubsequence(s):
#     count=1
#     for i in range(len(s)-1):
#         if s[i]!=s[i+1]:
#             count+=1
#     print(count)
# countsubsequence("aabbcd")

#parenthesis
# def parenthesis(s):
#     d={'(':')','[':']','{':'}'}
#     stack=[]
#     for i in s:
#         if i in d.keys():
#             stack.append(i)
#         elif i in d.values():
#             if not stack:
#                 print("Not balanced")
#                 return
#
#             top=stack.pop()
#             if d[top]!=i:
#                 print("Not balanced")
#                 return
#
#     if not stack:
#         print("Balanced")
#     else:
#         print("Not balanced")
#
# s=input("Enter:")
# parenthesis(s)