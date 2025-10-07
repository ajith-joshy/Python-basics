def decorator(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner

@decorator
def sub(a,b):
    #if a<b:
    #   a,b=b,a
    return a-b

print(sub(10,5))
print(sub(5,10))

#write a decorator function to check whether the second operand is zero before division
def decorator(fun):
    def inner(a,b):
        if b==0:
            return "error"
        else:
            return fun(a,b)
    return inner

@decorator
def div(a,b):
    return a/b
print(div(10,5))
print(div(10,0))