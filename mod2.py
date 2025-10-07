# import mod1
#
# mod1.msg()
#
# print(mod1.x)

# from mod1 import *
# msg()
# print(x)

#from package import module
from ABCD import mod1
mod1.msg()
#another method
from ABCD.mod1 import *
msg()
#import aliasing
from ABCD import mod1 as A
A.msg()