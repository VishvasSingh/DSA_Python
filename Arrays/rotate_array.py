from typing import List


"""

______________________________________________________________________________


https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

______________________________________________________________________________


"""

"""
______________________________________________________________________________

Brute force approach:
Copy the elements to two different arrays and then merge those two arrays 
for the final solution array
______________________________________________________________________________

"""
# def rotate_array(nums: List[int], k: int):
#     left_array = []
#     right_array = []
#     if k >= len(nums):
#       k = k % len(nums)
#
#     for i in range(len(nums)-k):
#         left_array.append(nums[i])
#
#     for i in range(len(nums)-k, len(nums)):
#         right_array.append(nums[i])
#
#     nums.clear()
#
#     for num in right_array:
#         nums.append(num)
#
#     for num in left_array:
#         nums.append(num)


"""
______________________________________________________________________________

Optimized approach:
Copy the elements to two different arrays and then merge those two arrays 
for the final solution array
______________________________________________________________________________

"""

def reverse(array: List[int], start: int, end: int):
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


def rotate_array(nums: List[int], k: int):
    if k >= len(nums):
        k = k % len(nums)

    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(nums)
    rotate_array(nums, k)
    print(nums)