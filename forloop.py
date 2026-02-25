#while -else
i=1
while(i<=5):
    print(i)
    i=i+1
else:
    print("hello")
print()

#for-else
for i in range(1,6,1):
    print(i)
else:
    print("hello")

#check whether a number is prime or not
n=int(input("Enter the number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")#for 1 and negative numbers

