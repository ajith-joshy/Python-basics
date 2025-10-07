#Given a list
# l=['dog','cat','sheep','tiger','lion','bear']
# for i in l:
#     print(i)

# #given a list
# l=[['dog','cat','sheep'],['tiger','lion','bear']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)

#Given a dictionary
d={1:['dog','cat','sheep'],2:['tiger','lion','bear']}
# print each items
for i in d.values():
    print(i)
    for j in i:
        print(j)
print()

#Given a list
l=['apple','orange','pineapple']
#print each character from each word
for word in l:
    print (word)
    for char in word:
        print(char)