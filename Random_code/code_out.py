A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))


print("A0:", A0)
print("\n")

A1 = range(10)

print("A1:",A1)
print("\n")


A2 = sorted([i for i in A1 if i in A0])


print("sorted([i for i in A1 if i in A0])")

print(A2)
print("\n")


A3 = sorted([A0[s] for s in A0])

print("sorted([A0[s] for s in A0])")
print (A3)
A4 = [i for i in A1 if i in A3]

print ("[i for i in A1 if i in A3]")
print(A4)
A5 = [[i,i*i] for i in A1]
print("[[i,i*i] for i in A1]")
print(A5)
