import numpy as np
print(np.pi)
print(np.sin(np.pi/4))
print("hello world")
listman = [1,3,'hi',8.5]
print(listman)
print(listman[1:3])
list_range = list(range(1,100))
print(list_range[10:14])

tupleman = (3,4,5)
print(tupleman)

list_to_tuple = tuple(listman)
print(list_to_tuple)

dictman = {'a':1,'b':2}
print(dictman)
print(dictman['a'])

setman ={4,5,6}
print(setman)
print(list(setman)[2])