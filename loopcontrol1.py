#normal
s="hello"
for i in s:
    print(i,end=" ")
print()

#break
s="hello"
for i in s:
    if i=='l':
        break
    print(i,end=" ")
print()

#continue
s="hello"
for i in s:
    if i=='l':
        continue
    print(i,end=" ")
print()

#given
s="Python is a programming language"
#print the string upto a specific character(including that character)
for i in s:
    print(i, end=" ")
    if i=='m':
        break
print()

#Given
fruits=['banana','apple','orange','pineapple','mango']
#iterate through the sequence and print each fruitname.exit the loop if fruitname="pineapple"
for i in fruits:
    if i=='pineapple':
        break
    print(i,end=" ")
print()
#iterate through the sequence print each fruitname.skip the iteration if fruitname='apple'
for i in fruits:
    if i=='apple':
        continue
    print(i,end=" ")
print()

#given a list
l=[45,67,12,90,78,10]
#print all elements except multiples of 3(using continue)
for i in l:
    if i%3==0:
        continue
    print(i,end=" ")
print()

#given
colors=['red','green','orange','blue','black','yellow']
#print the first occurence of colorname starting with 'b'
for i in colors:
    print(i, end=" ")
    if i[0]=='b':
        break
print()