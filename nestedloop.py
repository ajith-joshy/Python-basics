# #Nested loop
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()
# print()
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# print()
#
# for i in range(1,6):
#     for j in range(1,6):
#         print((i,j),end=" ")
#     print()
# print()
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=" ")
#     print()
# print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()
# print()
#
# for i in range(1,4):
#     for j in range(1,4):
#         print("#",end=" ")
#     print()
# print()
#
# for i in range(1,8,2):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
# print()
#
# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
# print()
#
# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
# print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print()
#
# for i in range(2,9,2):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# print()
#
# for i in range(1,8,2):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# print()

l=['kelly','emy','alen']
for i in l:
    for j in range(1,4):
        print(i,end=" ")
    print()

for i in range(1,4):
    print(i)
    for j in range(1,4):
        print(j,end=" ")
    print()
print()

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(2,9,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(1,8,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(1,9):
    for j in range(1,i+1):
        if j%2==0:
            print(2,end=" ")
        else:
            print(1,end=" ")
    print()
print()

for i in range(1,6):
        for j in range(1,6):
            if i==j:
                print(i,end=" ")
            else:
                print(0,end=" ")
        print()
print()

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()
print()

k=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
    k+=1
    print()
print()

for i in range(1,5):
    k = 65
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()
print()

k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    k=k-2
    for j in range(1,i+1):
        print("*",end="   ")
    print()
k=0
for i in range(4,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    k=k+2
    for j in range(1,i+1):
        print("*",end="   ")
    print()
print()

for i in range(1,5):
    for p in range(1,i+1):
        print("*",end=" ")
    print()
for j in range(3,0,-1):
    for q in range(1,j+1):
        print("*",end=" ")
    print()
print()

k=3*2
for i in range(1,5):
    for p in range(1,i+1):
        print("*",end=" ")
    k=k-2
    print()
k=0
for j in range(3,0,-1):
    for q in range(1,j+1):
        print("*",end=" ")
    print()
print()

