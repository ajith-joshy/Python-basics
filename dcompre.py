#dictionary comprehension
l=[1,2,3,4]
new={i:i**2 for i in l}
print(new)

#given a string
s="python is a programming language"
#create a dictionary
#where keys are words and values are length of each word
d={i:len(i) for i in s.split()}
print(d)

#Given a list
l=[1,1,2,3,4,5,6,6,7,7]
#create a new list with no duplicates
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
#using comprehension
new=[i for i in l if i not in new]
print(new)

#Given a list
#l=[10,20,30,40]
#create a dictionary where  keys are index and values are numbers in the given list l
#d={}
