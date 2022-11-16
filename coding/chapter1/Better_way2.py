import os
import sys

# Wrong
import sys, os

# Correct
from subprocess import Popen, PIPE

# Sys.apth
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# explicit relative imports
from . import silbing
from .sibling import example

# import a class from a class-containing module
from myclass import MYCLASS
from foo.bar.yourclass import YOURCLASS

# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...

# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

# Correct
if foo == 'blah':
    do_blah_thing()
for x in lst:
    total += x
while t < 10:
    t = delay()

# Wrong:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()


# 클래스 메소드 타입
class MethodTypes:
    
    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()