import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(type(a))

b = np.array([[1,2,3,4],[3,4,5,6],[9,7,4,7]])
print(b)
print(type(b))
print(len(b))

# creating some arrays 

c = np.zeros(4)  # this array can produce an array of zeroes 
print(c)

d = np.ones(5)   # this array can produce an array of ones  
print(d)

e = np.empty(5)  # this array can produce an array of empty 
print(e)

f = np.arange(9)  # this array will produce an array of 1 to 9
print(f)

g = np.arange(2,20)   # with specific range of elements 
print(g)

h = np.arange(2,20,2)   # continueu array 
print(h)

i = np.linspace(0,20,num=7)   #  linear spaced elements 
print(i)