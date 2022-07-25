Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mass = 5420
>>> acceleration = 9.89
>>> weight = mass*acceleration
>>> print(weight)
53603.8
>>> type(acceleration)
<class 'float'>
>>> type(mass)
<class 'int'>
>>> type(weight)
<class 'float'>
>>> m = 67
>>> v = 28
>>> u = 10.63
>>> t = 13
>>> f = m*(v-u)/t
>>> print(f)
89.52230769230768
>>> type(f)
<class 'float'>
>>> type(m)
<class 'int'>
>>> type(v)
<class 'int'>
>>> type(u)
<class 'float'>
>>> type(t)
<class 'int'>
>>> u = 15
>>> a = 12
>>> t = 5
>>> s = ut+(a*t**2)/2
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s = ut+(a*t**2)/2
NameError: name 'ut' is not defined
>>> s = ut+0.5(a*t**2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s = ut+0.5(a*t**2)
NameError: name 'ut' is not defined
>>> s = (u*t)+(a*t**2)/2
>>> print(s)
225.0
>>> 2s = (2*u*t)+(a*t**2)
SyntaxError: invalid syntax
>>> 2*s = (2*u*t)+(a*t**2)
SyntaxError: can't assign to operator
>>> type(s)
<class 'float'>
>>> 
