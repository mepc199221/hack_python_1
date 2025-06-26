"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    result = [i for i in range(5, -1, -1)]
    return result  

print(fn_hack_7())  # Output: [5, 4, 3, 2, 1, 0]