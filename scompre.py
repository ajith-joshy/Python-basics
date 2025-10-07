#set comprehension
#given a string
s='hello world'
new={i for i in s}
print(new)

#print without duplicates
new={i for i in s if i!=" "}
print(new)