from typing import List

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

https://leetcode.com/problems/pascals-triangle/
"""

def generate(nums_rows: int) -> List[List[int]]:
    result = [[1]]

    for i in range(1, nums_rows):
        temp = list()
        for j in range(len(result[i-1])-1):
            temp.append(result[i-1][j]+result[i-1][j+1])
        result.append([1, *temp, 1])

    return result


if __name__ == "__main__":
    print(generate(5))
