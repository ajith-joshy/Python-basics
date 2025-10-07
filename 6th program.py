#write a program to interchange or swap two numbers

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# a,b=b,a
# print("a=",a)
# print("b=",b)

#using temporary variable

a=int(input("enter a:"))
b=int(input("enter b:"))
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
