#LAMBDA
#
# #addition of two numbers
# s=lambda a,b:a+b
# print(s(45,45))
#
# #define lambda function to read the name from a dictionary
# d={'name':'arun','age':23}
# n=lambda x:x['name']
# print(n(d))
#
# #define lambda function to read the author from a list
# l=['book1','john',300,'english']
# a=lambda x:x[1]
# print(a(l))
#
# #define a function to print the first letter from a string
# s="python"
# f=lambda x:x[0]
# print(f(s))
#
# #define a lambda function to add 3 numbers
# add=lambda a,b,c:a+b+c
# print(add(3,4,5))
#
# #define a lambda function to find the cube of a number
# cube=int(input("Enter the number:"))
# c=lambda x:x**3
#print(c(cube))

#MAP function
# l=[1,2,3,4,5]
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))

#create a list of cubes from the given list
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))

#create a list of names
# l=[{'name':'arun','age':23},{'name':'amal','age':24},{'name':'anu','age':26}]
# print(list(map(lambda x:x['name'],l)))

#create a list of authors
# d=[['book1','john',200],['book2','mike',300],['book3','sam',500]]
# print(list(map(lambda x:x[1],d)))

#create a list of length
# colors=['red','green','orange','yellow','blue']
# print(list(map(lambda x:len(x),colors)))

#create of list of square roots
# l=[34,81,49,16]
# print(list(map(lambda x:x**0.5,l)))


#FILTER function

# l=[34,77,15,90,56]
# #create a list of even values
# print(list(filter(lambda x:x%2==0,l)))
#
# #create a list of odd values
# print(list(filter(lambda x:x%2!=0,l)))
#
# #create a list of numbers greater than 50
# print(list(filter(lambda x:x>50,l)))
#
# #create of list of numbers that are divisible by 3
# print(list(filter(lambda x:x%3==0,l)))
#
# #create a list of even numbers greater than 50
# print(list(filter(lambda x:x%2==0 and x>50,l)))


#REDUCE function

l=[1,2,3,4]

#sum of given sequence
import functools
print(functools.reduce(lambda x,y:x+y,l))

#product of given sequence
import functools
print(functools.reduce(lambda x,y:x*y,l))

#Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#sum of positive even numbers
pe=(list(filter(lambda x:x>0 and x%2==0,l)))
import functools
print(functools.reduce(lambda x,y:x+y,pe))
#sum of positive odd numbers
po=(list(filter(lambda x:x>0 and x%2==0,l)))
import functools
print(functools.reduce(lambda x,y:x+y,po))
#sum of  negative even numbers
ne=(list(filter(lambda x:x<0 and x%2==0,l)))
import functools
print(functools.reduce(lambda x,y:x+y,ne))
#sum of negative odd numbers
no=(list(filter(lambda x:x<0 and x%2!=0,l)))
import functools
print(functools.reduce(lambda x,y:x+y,no))
#count of positive numbers
# cp=(list(filter(lambda x:x>0,l)))
# import functools
# print(functools.reduce(lambda x:x.count(),cp))
# #count of negative numbers
# print(list(filter(lambda x:x<0,l)))
# import functools
# print(functools.reduce(lambda x:x.count(),l))

#Given a list
# l=['python','coding','is','easy','and','fun']
# create a string "python coding is easy and fun" from the given list l
# import functools
# print(str(functools.reduce(lambda x:type(x)==str,l)))