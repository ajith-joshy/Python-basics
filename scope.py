#Global
# x=20    #global_variable
# print("outside function",x)
# def f():
#     print("within function",x)
# f()
# print("outside function",x)

#local
# def f():
#     x=20    #local_variable
#             #can only be accessible inside the function
#     print("Inside function",x)
# f()
# print("outside function",x) #error

# def f1():
#     global x
#     x=20    #local
#     print("inside f1",x)
#
# def f2():
#     y=30    #local
#     print(x)
#     print("inside f2",y)
#
# f1()
# f2()

#nonlocal
def outer():
    x=20    #enclosing or nonlocal
            #can be accessible from both inner and outer function
    print("inside outer",x)
    def inner():
        y=30    #local variable
                #can be accessible from inner function only
        print("Inside Inner",x)
    inner()
    print("inside outer",x)
outer()
