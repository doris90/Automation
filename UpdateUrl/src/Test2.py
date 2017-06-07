'''
Created on 2017-6-6

@author: yushao
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print (factorial(10))
print ("10000000000000000000000000000000000000000")