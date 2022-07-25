Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> exam = ["ben", 53, "kunle", 72, "joy", 61]
>>> exam
['ben', 53, 'kunle', 72, 'joy', 61]
>>> exam[5] = 64
>>> exam
['ben', 53, 'kunle', 72, 'joy', 64]
>>> exam[0] = "bayo"
>>> exam
['bayo', 53, 'kunle', 72, 'joy', 64]
>>> exam + ["chris", 80]
['bayo', 53, 'kunle', 72, 'joy', 64, 'chris', 80]
>>> exam + ["debby", 70]
['bayo', 53, 'kunle', 72, 'joy', 64, 'debby', 70]
>>> del(fam[0])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del(fam[0])
NameError: name 'fam' is not defined
>>> del(exam[0])
>>> exam
[53, 'kunle', 72, 'joy', 64]
>>> del(exam[0])
>>> exam
['kunle', 72, 'joy', 64]
>>> x = ["a","b","c"]
>>> y = x
>>> y[0] = k
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    y[0] = k
NameError: name 'k' is not defined
>>> y[0] = "k"
>>> x
['k', 'b', 'c']
>>> y
['k', 'b', 'c']
>>> 
