#-*- coding: utf-8 -*-
print ("201502077/유예지")
def sum(n):
    if n == 1: return 1
    return n + sum(n-1)

def fibonacci(n):
    if n == 1 or n==2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n ==0: return 1
    return n * factorial(n-1)

def decimal_to_binary(n):
    if n==0 or n==1: return n;
    return (decimal_to_binary(n/2)*10) + (n%2)

def TestRecursionFunction():
    print factorial(10)
    print sum(100)
    print fibonacci(10)
    print decimal_to_binary(15)
    
TestRecursionFunction()
