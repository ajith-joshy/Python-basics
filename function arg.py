#positional arguments
def f(name,age):
    print("Name:",name)
    print("Age:",age)
f("Arun",23)

#keyword arguments
def f(name,age):
    print("Name:",name)
    print("Age:",age)
f(name="Arun",age=23)

#default arguments
def f(name,age=25):
    print("Name",name)
    print("Age:",age)
f('Arun')
f('arun')

#arbitary arguments
def f(*args):
    print(args)
f(10,20,30)
f(10,20,30,40)
f(1,2,3,4,5,6,7,8,9)

def f(**kwargs):
    print(kwargs)  #it represents dictionary
f(a=10,b=20,c=30)
f(d=40,e=50)