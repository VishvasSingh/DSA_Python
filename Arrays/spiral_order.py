from typing import List
"""
Print matrix in spiral order

https://leetcode.com/problems/spiral-matrix/
"""


def spiral_order(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix[0]), len(matrix)
    upper_end, lower_end, left_end, right_end = 0, n, 0, m
    result = []

    while left_end < right_end and upper_end < lower_end:
        # going right first
        for j in range(left_end, right_end):
            result.append(matrix[upper_end][j])

        # once right is complete, top row is over, that means upper end will increase by 1
        upper_end += 1

        # going down
        for i in range(upper_end, lower_end):
            result.append(matrix[i][right_end-1])

        # once going down is complete, right column is over, that means, right end will decrease by 1
        right_end -= 1

        # going left
        if upper_end >= lower_end:
            break

        for j in range(right_end-1, left_end-1, -1):
            result.append(matrix[lower_end-1][j])

        # once going left is complete, that means bottom row is over, hence lower end will decrease by 1
        lower_end -= 1

        # going up
        if left_end >= right_end:
            break

        for i in range(lower_end-1, upper_end-1, -1):
            result.append(matrix[i][left_end])

        # once going up is complete, that means left column is over, left end will increase by 1

        left_end += 1

    return result


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_order(matrix))



