import time

def memoization(func):
    dic = {}
    # print("decorator called")
    
    def wrapper(*args, **kwargs):
        # print("args", args)
        if args in dic:
            return dic[args]
        else:
            dic[args] = func(*args, **kwargs)
            # print("dic ", dic)
        return dic[args]
    
    return wrapper

@memoization
def fib(n):
    # print("function called")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)

n = 35

s = time.time()
print("Nth fibbonaci number is ", fib(n))
e = time.time()
print("Time taken with memoization is ", e - s)

s = time.time()
print("Nth fibbonaci2 number is ", fib2(n))
e = time.time()
print("Time taken without memoization is ", e - s)

