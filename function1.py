#write a program to check whether a number is perfect or not
def perfect_number():
    n=int(input("Enter number:"))
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if(sum==n):
        print(n,"is a perfect square")
    else:
        print(n,"not a perfect square")

perfect_number()

#Define a function to convert celsius temperature into farenheit
def celsius_farenheit():
    c=int(input("Enter celsius temperature:"))
    f=(c*9/5)+32
    print(f,"is the farenheit temperature")

celsius_farenheit()