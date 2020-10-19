Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> friends = [“islam”, 1[“muhammed”,2], True, False]
SyntaxError: invalid character in identifier
>>> friends= ["friends = [“islam”, 1[“muhammed”,2], True, False]
	  
SyntaxError: EOL while scanning string literal
>>> friends = ["islam", 1["muhammed",2], True, False]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    friends = ["islam", 1["muhammed",2], True, False]
TypeError: 'int' object is not subscriptable
>>> friends = [1, "FodaCode", True, False,[1, "Muhammad"]]
>>> print(friends)
[1, 'FodaCode', True, False, [1, 'Muhammad']]
>>> friends = ["islam", 1,["muhammed",2], True, False]
>>> print(friends)
['islam', 1, ['muhammed', 2], True, False]
>>> friends = [1, "Foda", True, False,[1, "Muhammad"]]print(friends)
SyntaxError: invalid syntax
>>> friends = [1, "Foda", True, False,[1, "Muhammad"]]
>>> print(friends)
[1, 'Foda', True, False, [1, 'Muhammad']]
>>> 
