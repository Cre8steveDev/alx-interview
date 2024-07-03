array_one = [5, 3, 9, 10, 482, 80, 3, 0, 1, 14, 12]
array_two = [19, 33, 12, 9, 34, 6, 123, 8]

import time
from typing import List, Union


"""Binary Search"""

def binary_search(haystack: List, needle: Union[int, str]):
    low = 0
    high = len(haystack) - 1
    
    range_list = len(haystack)//2
    
    for _ in range(range_list):
        if haystack[low] == needle:
            return {"needle": haystack[low], "index": low}
        
        if haystack[high] == needle:
            return {"needle": haystack[high], "index": high}
        
        low += 1
        high -= 1
        
    return None


start_1 = time.time()
result_1 = binary_search(array_one, 10)
end_1 = time.time()


print(result_1)
print(f"Time taken: {end_1 - start_1}")


start_2 = time.time()
result_2 = binary_search(array_two, 123)
end_2 = time.time()

print(result_2)
print(f"Time taken: {end_2 - start_2}")

