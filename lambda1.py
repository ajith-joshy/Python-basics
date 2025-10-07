#Q1.
phone_book={'john':['8592790000','john@gmail.com'],
'Bob':['7994880000','bob@gmail.com'],
'Tom':['9749552647','tom@gmail.com']}
#Extract all email address using map() function
print(list(map(lambda x:x[1],phone_book.values())))

#Q2.Given'
l=[10,'hello',9.8,'abc',11.2,'arun']
#count of floating point values
f=list(filter(lambda x:type(x)==float,l))
print()