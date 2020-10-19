'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
print(names,jobs)
'''
#use function extend
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.extend(jobs)
print (names)
'''

#use function append
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.append("Ali")
print (names)
'''
#use function insert
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.insert(1,"hatem")
print (names)
'''
#use function remove
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.remove("Ahmed")
print (names)
'''
#use function remove
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.remove("programming")
print (names)
'''
#use function clear
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.clear()
print (names)
'''
#use function pop
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
names.pop()
print (names)
#لو عاوز اخزن القيمة في Variable
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
pop = names.pop()
print (pop)
'''
#use function index 
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
print(names.index("Muhammad"))
'''
#use function count عدد اللى اسمهم
#muhammad
#داخل list
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
jobs=["programming" , "accountant", "desginer", "QC", "Software Engnir"]
print(names.count("Muhammad"))
'''
#use function sort
'''
names = [10,  1, 4, 6, 7]
names.sort()
print(names)
'''
#use function copy 
'''
names = ["Muhammad", "Ahmed" , "Shady", " Ramy", "YaQOp"]
users = names
names.append("ali")
print(users)
print(names)

'''



































