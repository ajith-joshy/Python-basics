# #list comprehension
# l=[1,2,3,4]
# new=[i**2 for i in l]   #for each iteration adds i**2 to new list where i takes value from given list 'l'
# print(new)
#
# new=[i**3 for i in l]   #in each iteration adds i**3 to new list where i takes value from given list 'l'
# print(new)
#
# new=[5 for i in l]  #in each iteration adds 5 to new list where i takes value from given list 'l'
# print(new)
#
# #given a list
# l=['apple','orange','pineapple']
# #create a new list with first letter from each word
# new=[i[0] for i in l]
# print(new)

# #given a list
# l=[12,75,67,13,56,11]
# #create a new list with even values
# new=[i for i in l if i%2==0]
# print(new)
# #create a new list with odd values
# new=[i for i in l if i%2!=0]
# print(new)
# #create a new list with numbers less than 50
# new=[i for i in l if i<50]
# print(new)

#Given a list
fruits=['apple','banana','orange','pineapple','avocado']
#create a new list with elements whose length >5
new=[i for i in fruits if len(i)>5]
print(new)

##Given a list
l=[12,39,'hello',8.7,-98,-11,5,'python']
#create a new list with only string values
new=[i for i in l if type(i)==str]
print(new)
# create a new list with only positive values
new=[i for i in l if type(i)==int and i>0]
print(new)
#create a new list with float values
new=[i for i in l if type(i)==float]
print(new)

#create a list with elements whose value is divisible by 3 in the range (1,100)
n=[i for i in range(1,101) if i%3==0]
print(n)

#Given a string
s="python programming"
#create a new list with only vowels
v='aeiou'
new=[i for i in s if i in v]
print(new)

#given a dictionary
d={101:'Arun',102:'Amal',103:'Anu'}
#create a new list with only names
new=[i for i in d.values()]
print(new)

#given a dictionary
d={'a':10,'b':15,'c':20,'d':25}
#create a new list only even values
new=[i for i in d.values() if i%2==0]
print(new)