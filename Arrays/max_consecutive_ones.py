from typing import List

"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

https://leetcode.com/problems/max-consecutive-ones/

"""


def max_consecutive_ones(nums: List[int]) -> int:
    max_count = 0
    curr_count = 0
    for each_num in nums:
        if each_num == 1:
            curr_count += 1
        else:
            curr_count = 0

        max_count = max(max_count, curr_count)

    return max_count


if __name__ == "__main__":
    nums = [1,1,1,0,0,1,0,1,1,1,1]
    print(max_consecutive_ones(nums))
