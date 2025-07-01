"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    response_result = []
    
    i = 0 
    
    while i < len(result):
        response_result.append(result[i])
        response_result.append('@')
        i += 1
        
    return response_result

print(fn_hack_9())  # Output: [1, '@', 2, '@', 3, '@']