from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


https://leetcode.com/problems/two-sum/

"""


def two_sum(nums: List[int], target: int) -> List[int]:
    mapping = dict()
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in mapping:
            return [mapping.get(comp), i]

        else:
            mapping[nums[i]] = i

    return [0, 0]


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 25, 16, 58, 1, 2, 68]
    target = 68+25

    print(two_sum(nums, target))
