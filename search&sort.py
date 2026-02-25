# linear search
# def linear():
#         l=list(map(int,input("Enter the list of numbers:").split()))
#         n=int(input("Enter the number to be searched:"))
#         found=False
#         for i in range(len(l)):
#             if l[i]==n:
#                 print(n,"was found at position",i)
#                 found=True
#         if not found:
#             print("element not found")
# linear()

# Binary Search
# def binary(l,n):
#     low=0
#     high=len(l)-1
#     while low<=high:
#         mid=(low+high)//2
#         if l[mid]==n:
#             print(n,'element found at position',mid)
#             return
#         elif n<l[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     else:
#         print('element not found')
# binary([0,1,2,3,4,5],2)

#bubble sort
# def bubble(l):
#     n=len(l)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     print("Sorted list:",l)
# bubble([5,4,3,2,1])

#selection sort
# l=list(map(int,input('Enter the elements:').split()))
# n=len(l)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if l[j]<l[min_index]:
#             min_index=j
#     l[i],l[min_index]=l[min_index],l[i]
# print(l)
