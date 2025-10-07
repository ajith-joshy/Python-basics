# print python for 5 times
# i=1
# while(i<=5):
#     print('python')
#     i=i+1

# print HELLO WORLD 10 times
# i=1
# while(i<=10):
#     print(i,"Hello World")
#     i+=1

#print 1-10 numbers
i=1
while(i<=10):
    print(i,end=" ")
    i+=1
print()

#1 3 5 7 9 11
i=1
while i<=11:
    print(i,end=" ")
    i+=2
print()

#2 4 6 8 10
i=2
while(i<=10):
    print(i,end=" ")
    i+=2
print()

#10 20 30 40 50
i=10
while i<=50:
    print(i,end=" ")
    i+=10
print()

#1 4 9 16 25 36
i=1
while(i<=6):
    print(i**2,end=" ")
    i+=1
print()

#100,101,...,200
i=100
while(i>=200):
    print(i)
    i+=1
print()

#5,4,3,2,1
i=5
while(i>=1):
    print(i,end=" ")
    i-=1
print()

#8,6,4,2,0
i=8
while(i>=0):
    print(i,end=" ")
    i=i-2
print()

#100,200,...,1000
i=100
while(i<=1000):
    print(i,end=" ")
    i+=100
print()

#4,9,14,19,24,29,34
i=4
while(i<=34):
    print(i,end=" ")
    i+=5
print()

#3 12 48 192 768 3072
i=3
while(i<=3072):
    print(i,end=" ")
    i=i*4
print()

#print all 3-digit numbers
i=100
while(i<=999):
    print(i,end=" ")
    i+=1
print()

#print all 3-digit numbers divisible by 3
i=100
while(i<=999):
    if(i%3==0):
        print(i,end=" ")
    i+=1
print()

#print all 3-digit numbers divisible by 2 and 3
i=100
while(i<=999):
    if(i%3==0 and i%2==0):
        print(i,end=" ")
    i+=1
print()

#20,18,16,14....0
i=20
while(i>=0):
    print(i,end=" ")
    i=i-2
print()

#print those numbers that are divisible by 3 and 5 in the range(200,400)
i=200
while(i<=400):
    if(i%3==0 and i%5==0):
        print(i,end=" ")
    i+=1
print()

#count of those numbers that are divisible by 3 and 5 in the range(200,400)
i=200
count=0
while i<=400:
    if i%3==0 and i%5==0:
        count=count+1
    i+=1
print(count)

#count of those numbers that are divisible by 7 in the range(1500,2700)
i=1500
count=0
while i<=2700:
    if(i%7==0):
        count=count+1
    i+=1
print(count)

#sum of first five numbers(1,2,3,4,5)
i=1
sum=0
while i<=5:
    sum=sum+i
    i+=1
print(sum)

#product of first five numbers(1,2,3,4,5)
i=1
product=1
while i<=5:
    product=product*i
    i+=1
print(product)

#sum of numbers from 200-400
i=200
sum=0
while i<=400:
    sum+=i
    i=i+1
print(sum)

#sum of squares of numbers from 1-10
i=1
sum=0
while(i<=10):
    sum+=i**2
    i=i+1
print(sum)

#sum of cubes of numbers from 1-10
i=1
sum=0
while(i<=10):
    sum+=i**3
    i=i+1
print(sum)

#product of even numbers from 1-100
i=1
product=1
while i<=100:
    if i%2==0:
        product=product*i
    i=i+1
print(product)

#sum and count of numbers that are divisible by 3 in the range(1,50)
i=1
sum=0
count=0
while i<=50:
    if i%3==0:
        sum=sum+i
        count=count+1
    i=i+1
print("The count of numbers divisible by 3 in the range 1-50:",count)
print("The sum of numbers divisible by 3 in the range 1-50:",sum)

#factorial of a number
# i=1
# n=int(input("Enter the number:"))
# fact=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)

# #multiplication table of a number
# n=int(input("Enter the number:"))
# i=1
# while i<=10:
#     print(i,"*",n,"=",i*n)
#     i=i+1

#Factors of a number
n=int(input("Enter a number:"))
i=1
while(i<=n):
    if(n%i==0):
        print(i)
    i=i+1