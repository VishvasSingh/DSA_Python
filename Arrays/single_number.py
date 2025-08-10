from typing import List

"""
Problem Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

https://leetcode.com/problems/single-number/

"""


def single_number(nums: List[int]) -> int:
    single_num = 0
    for each_num in nums:
        single_num = each_num ^ single_num

    return single_num


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    single_num = single_number(nums=nums)
    print(single_num)