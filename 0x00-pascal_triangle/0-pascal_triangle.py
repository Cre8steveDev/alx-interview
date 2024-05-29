"""
Writing an efficient Solution to solve
The Pascal Triangle Interview Question in
ALX Backend Specialization Round
"""


def pascal_triangle(n):
    if n <= 1:
        return [] if n <= 0 else [[1]]

    array = [[1], [1, 1]]

    if n == 2:
        return array

    arr_t = 1
    for i in range(2, n):
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


if __name__ == "__main__":
    print(pascal_triangle(1))
