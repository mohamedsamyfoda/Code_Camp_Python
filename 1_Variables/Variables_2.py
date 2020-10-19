Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = '7'
>>> type (s)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type (s)
NameError: name 's' is not defined
>>> type (x)
<class 'int'>
>>> type (y)
<class 'str'>
>>> s = 'muhammad foda'
>>> y = 8
>>> f = 5.9
>>> 
>>> print(type(s))
<class 'str'>
>>> print(type(y))
<class 'int'>
>>> print(type(f))
<class 'float'>
>>> 
>>> 
>>> x = 6; y=2
>>> x
6
>>> y
2
>>> x, y = 3,1
>>> x
3
>>> y
1
>>> 
>>> 
>>> x = 6; y=2
>>> print(type(x,y))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(type(x,y))
TypeError: type() takes 1 or 3 arguments
>>> print(type(x),(y))
<class 'int'> 2
>>> type x ; type y
SyntaxError: invalid syntax
>>> type (x) ; type (y)
<class 'int'>
<class 'int'>
>>> 
