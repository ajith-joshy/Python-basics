#wap to check whether positive-even/positive-odd/negative-even/negative-odd
# n=int(input("Enter the number:"))
# if(n>0):
#     if(n%2==0):
#         print(n,"is positive even")
#     else:
#         print(n,"is positive odd")
# else:
#     if(n&2==0):
#         print(n,"is negative even")
#     else:
#         print(n,"is negative odd")

#Q2
code=int(input("Enter the code:"))
amount=int(input("Enter the amount:"))
if(code==1):
    if(amount>1000):
        print("Final amount to pay is",amount*90/100)
    else:
        print("Final amount to pay is",amount)
elif(code==2):
    if(amount>100):
        print("Final amount to pay is",amount*95/100)
    else:
        print("Final amount to pay is",amount)
elif(code==3):
    if(amount>500):
        print("Final amount to pay is",amount*90/100)
    else:
        print("Final amount to pay is",amount)
else:
    print("Invalid input")