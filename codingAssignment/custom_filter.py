def custom_filter(func, sequence):
    ans = []
    for num in sequence:
        if func(num):
            ans.append(num)
    
    return ans
        
        
def is_even(num):
    return False if num % 2 == 1 else True

nums = [1, 2, 3, 4, 5, 6, 7]

print("output from custom filter is ", custom_filter(is_even, nums))


print("output from real filter is ", list(filter(is_even, nums)))

print("output from custom filter is ", custom_filter(lambda x : x%3 == 0, nums))


print("output from real filter is ", list(filter(lambda x : x%3 == 0 , nums)))