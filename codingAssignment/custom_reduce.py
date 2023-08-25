import functools
import operator

def custom_reduce(func, sequence):
    isequence = iter(sequence)
    ans = next(isequence)
    for val in isequence:
        ans = func(ans, val)
    return ans
    


lis = [1, 3, 5, 6, 2]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))


print("The sum of the list elements is custom: ", end="")
print(custom_reduce(lambda a, b: a+b, lis))
 
 
