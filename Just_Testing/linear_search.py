array_one = [5, 3, 9, 10 , 482, 80, 3, 0, 1, 14]
array_two = [19, 33, 12, 9, 34, 6, 123, 8]

import time
from typing import List, Union


"""Linear Search"""

def linear_search(haystack: List, needle: Union[int, str]):
    for i in haystack:
        if i == needle:
            return i
    return None


start_1 = time.time()
result_1 = linear_search(array_one, 10)
end_1 = time.time()


print(result_1)
print(f"Time taken: {end_1 - start_1}")


start_2 = time.time()
result_2 = linear_search(array_two, 123)
end_2 = time.time()

print(result_2)
print(f"Time taken: {end_2 - start_2}")

