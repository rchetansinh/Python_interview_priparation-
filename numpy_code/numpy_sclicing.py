import numpy as np


#will start with array sclicing

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)

print(a[1:])

print("\n")

print(a[-1 : , 0])

#[[5,6]
# [8,9]]
print (a[1: , 1: ])


#sclicing with boolean

a = np.arange(12).reshape(4,3)
print(a)

b = a > 5
print(b)

print(a[b]) #whereever it's true it will return that value

#if i want to replce that all with other value

a[b] = 6

print(a)


