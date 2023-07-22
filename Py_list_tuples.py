# TUPLES (ordered sequence)
A = (1,2,3,4,5,6)
print(A)

# elements of a tuples: int, str, l=float, bolean

# Access elements via index
# A[0] = first element    -   A[-1] = last element
print(A[0])
print(A[-1])

# concatenate ( combine)
B= (7,8,9,10)
C= A + B
print(C)

# Slice tuples
A[0:3]
print(A[0:3])

# len
print(len(A))

# Tuples are immutable, to make changes, you need to create a new tuple
# to sort a tuple we need to create a new tupple
D= (4,10,5,1)
E = sorted(D)
print(E)

# Nesting = a tuple inside another tuple

ND = ( 1, 2, ('a','b'))
print(ND[2])
print(ND[2][1])

#LIST
# list are also an ordered sequence of elements but with square brackets
A = [ 1,2,3,4,5]
print([A])

# List are like tuples but mutable
# elements of a list: str, float, int, bolean)
# we can nest another list or tuple in a list

B=[1,2,[3,'a'],[4,'b']]
print(B[3][1])

# Access elements via index
print(B[0])
print(B[-1])

# List slicing
print(B[1:2])

# concatenate or combine list
L1 = B + [1,3,4]
print(L1)

# List are mutable so we can change it. Examples of methods we can use 
# .extend
L1.extend(['extend', 'is a method'])
print(L1)

# .append ( we add ONE element to the list)
A.append(['a','b','c'])
print(A)
A.extend(['d','e'])
print(A)

# We can change an element in a list
A[0] = "change a list"
print(A)
# delete an element of a list withn DEL command
del(A[0])
print(A)

# convert a string into a list 

Z= "convert to a list".split()
print(Z)

W = "A,B,C,D".split()
print(W)

# Aliasing = multiplie names refering to the same object
E= ["hard rock", 10,1.2]
F = E
E[0] = "banana"
print(E)

# Clone a list with the following syntax ( the new list will not change with
# changes of the original list)

G = [1,2,3]
H = G[:]
print(H)
G[0] = " if it's a clon it will not change"
print(H)

# more information needed about a python object use help command
help (A)



