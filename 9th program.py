#Q1
l= ["pasta", "noodles", "bread", "butter", "jam", "apple"]
l[2]="cookies"
print(l)
print("length of the list is:",len(l))
print("reverse of the string is:",l[::-1])
print("the last food item is:",l[-1])
print("the fifth food item is:",l[4])

#Q2
l1=[23,56,89,10,67,45,17]
l1[1],l1[5]=l1[5],l1[1]
print(l1)