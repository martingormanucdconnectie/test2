# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:15:52 2015

@author: mgorman
"""

### Setting up a function to print twice
def print_twice(bruce):
    print bruce
    print bruce
    
print_twice('spam')

print len("spammer")

### Exercise 2.3 Think Python Page 18 or 40 
start = ((6*3600)+(52*60))
run1 = ((8*60)+(15))
run2 = ((7*60)+(12))
end = start + run1 + (run2)*3 + run1
print end/60.00/60

## sum a list of numbers
numbers = [1,2,3,4,5,6,7,8,9]
h = 0
n = []
for i in numbers:       
    h = h + i
    n = [h]    
    print n
    
### strings
s = "fruit"[:]
print s

import random
for i in range(5):
    print random.random
    print random.randrange(10,20)
    print random.choice("abcd")
    print ""
    
############
    
import numpy as np;

x = np.array([4.0,5.0,6.0,10.0])    
print(x)

print(x.sum())    
print(x.mean())
print(x.std())
print(x.min())
print(x.max())
print(x.argmax())
print(x * 3)
print(x + 1)

y = np.array(range(10))
print y
z = np.array(range(10))+100
print z
print z.std()
    
zeros =np.zeros(4)
print(zeros)
ones = np.ones(6)    
print(ones)
five = ones * 6
print five

grid = np.linspace(0, 2, 9  )

print grid

a = np.linspace(100,200,8)
b = np.random.uniform(a)
print a

c = np.random.normal(100, 1, 20)
print c

m = np.ones((2,2))
print(m)
X = [[1,2,3],[2,1,3]]
X = np.array(X)
print X
#print X[2,2]    

n = range(2)
for i in n:
    print i

p = range(3)
for j in p:
    print j
    
print X[i,j]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    