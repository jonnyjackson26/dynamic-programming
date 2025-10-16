"""
This is my first time doing dynamic programming. 
In the first problem I find the minimum sum of continuous subarray in a given array. (linear time).
In the second problem I find the nth fibonacci number with dynamic programming.
These are challenge problems from the YouTube video "Dynamic Programming Explained (Practical Examples)" by Tech with Tim, which I watched

https://www.youtube.com/watch?v=Sz9yH-RDAgo&t=73s
"""

myArray = [1,-2,100,-15,100,4,-2,-4,1,-3]

def minsubarray(arr): #returns min and min_range
    min_sum = arr[0]
    current_sum = arr[0]
    start = end = s = 0
    for i in range(1, len(arr)):
        if arr[i] < current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]
        if current_sum < min_sum:
            min_sum = current_sum
            start = s
            end = i
    return min_sum, [start, end]

minimum,min_range=minsubarray(myArray)
print(f"The minimum subarray is {min_range}, summing to {minimum}")





#find the 35th fibonacci number (with memoization). 
#This makes it so I dont need to go down branches I've already been down

def fib(n, cache={}):
    if n<2:
        return n
    if n in cache:
        return cache[n]
    cache[n]=fib(n-1,cache) + fib(n-2, cache)
    return cache[n]

n=35
print(f"the {n}th fibonacci number is {fib(n)}")




