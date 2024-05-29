"""
Writing an efficient Solution to solve 
The Pascal Triangle Interview Question in 
ALX Backend Specialization Round
"""

def pascal_triangle(n): 
    if n <= 1:
      return [] if n <= 0 else [1]

    array = [[1], [1, 1]]
    
    if n == 2:
        return  array
    
    arr_t = 1
    for i in range(n):
        collector = []
        inner_arr_len = len(array[arr_t]) - 1
        
        collector.append(1)
        for j in range(inner_arr_len):
            slow, fast = array[arr_t][j], array[arr_t][j + 1]
            sum = slow + fast
            collector.append(sum)
        
        collector.append(1), array.append(collector)
        arr_t = arr_t + 1
        
    return array

# resulting_triangle = pascal_triangle(5)

# # Print Centralized 2D Array
# def print_centered_arr(pascals_triangle):
#   last_arr = pascals_triangle[-1]
#   max_width = len(' '.join(map(str, last_arr)))

#   for array in pascals_triangle:
#     row_str = ' '.join(map(str, array)).center(max_width)
#     print(row_str)

# print_centered_arr(resulting_triangle)

