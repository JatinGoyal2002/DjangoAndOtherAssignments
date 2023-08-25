def custom_map(func, *args, **kwargs):
    
    ans = []
    
    for value in zip(*args):
        ans.append(func(*value))
        
    return ans
    
def func(x, y, z):
    return x + y + z
    
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9] 

print("custom map, ",custom_map(lambda x,y, z : x + y + z, numbers1, numbers2, numbers3))

result = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
print(list(result))

numbers = (1, 2, 3, 4)

print("custom map, ",custom_map(lambda x: x + x, numbers))

result = map(lambda x: x + x, numbers)
print(list(result))

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
 
numbers = [1, 2, 3, 4, 5]

print("custom map, ",custom_map(double_even, numbers))
 
result = list(map(double_even, numbers))
 
print(result) 

result = custom_map(lambda x : x*2, [1,2,3])
print(result)