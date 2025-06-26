"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    response_result = []
    for item in result:
        response_result.append(item)
        response_result.append('@')
    return response_result  

print(fn_hack_9())  # Output: [1, '@', 2, '@', 3, '@']