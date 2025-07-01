"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 5
    while i >= 0:
        result.append(i)
        i -= 1
    return result

print(fn_hack_7())  # Output: [0, 1, 2, 3, 4, 5]