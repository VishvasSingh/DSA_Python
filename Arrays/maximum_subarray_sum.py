from typing import List

"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
(KADANE's Algo)

https://leetcode.com/problems/maximum-subarray/
"""


def max_subarray_sum(nums: List[int]) -> int:
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = max_subarray_sum(nums)
    print(max_sum)



