#Given
# s="Python is a programming language"
# ch=input("Enter the character:")
# print("Position of character ch is",s.find(ch))

#find the count of a specific ch
# ch=input("Enter the character:")
# print("Count of a specific character:",s.count(ch))

#given
# s="hello world"
# d={}
# for i in s:
#     if i!=" ":
#         d[i]=s.count(i)
# print(d)

#given
# s="python coding is easy and fun"
# d=s.split()
# for i in d:
#     if len(i)>5:
#         print(i)

#Given

l1=[12,45,67,89,90]
l2=[34,78,12,56,45]
#find the common elements
s1=set(l1)
s2=set(l2)
inter=("Common elements are",s1.intersection(s2))
print(inter)

l3=[12,45,67,89,90]
#find the max largest element from the list
largest=("largest element is",max(l3))
print(largest)
#find the second largest element from the list

#find the minimum element from the list
l4=[12,45,67,89,90]
minimum=("Smallest element is",min(l4))
print(minimum)

#find the second smallest element from the list
l4.sort()
print("Second larget is",l4[-2])
l5=[1,1,2,3,3,3,5,6,7,7]
#create dictionary where keys are numbers and values are count of each number
d={}
for i in l5:
    d[i]=l5.count(i)
print(d)

#Given
d={1:['Arun',23,30000],2:['Amal',26,50000],3:['Anu',24,20000],4:['Kiran',27,60000]}
#find the maximum salary
l=[]
for i in d.values():
    #print(i[2])
    l.append(i[2])
print(max(l))
print()

#given
s="python is a programming language"
#find the maximum length from the string
l=s.split()
max_length=max([len(i) for i in l])
print(max_length)
for i in l:
    if len(i)==max_length:
        print(i)
print()

#given a list
l=[12,45,67,89,23]
#find the maximum value from the list without using max() function
l.sort(reverse=True)
print("largest value is",l[0])
#or
max=l[0]
for i in l:
    if i>max:
        max=i
print(max)