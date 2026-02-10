from typing import List


"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

def longest_consecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_count = 0
    for num in nums:
        if num-1 not in nums_set:
            next_val = num + 1
            curr_count = 1
            while next_val in nums_set:
                curr_count += 1
                next_val += 1

            max_count = max(curr_count, max_count)

    return max_count


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longest_consecutive(nums))