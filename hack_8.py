"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result = result[1:4]  # Slicing to get elements at index 1, 2, and 3
    return result  

print(fn_hack_8())  # Output: [3, 5, 7]