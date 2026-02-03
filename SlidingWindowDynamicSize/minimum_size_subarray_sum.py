from typing import List

"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/minimum-size-subarray-sum/description/


Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

"""

"""
My O(N) solution
"""

# def min_subarray_len(target: int, nums: List[int]) -> int:
#     left = 0
#     curr_sum = 0
#     min_length = float('inf')
#
#     for right in range(len(nums)):
#         curr_sum += nums[right]
#         if curr_sum >= target:
#             min_length = min(min_length, right - left + 1)
#
#         while (curr_sum-nums[left]) >= target and left < right:
#             curr_sum -= nums[left]
#             left += 1
#             min_length = min(min_length, right - left + 1)
#
#     if min_length == float('inf'):
#         return 0
#
#     return min_length


"""
Cleaner Code:

"""


def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        # 1. Expand window
        current_sum += nums[right]

        # 2. Shrink window as much as possible while still valid
        while current_sum >= target:
            current_len = right - left + 1
            min_len = min(min_len, current_len)

            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len


"""
O(N log N) solution for array containing -ve elements

import bisect

def min_sub_array_len_nlogn(target: int, nums: List[int]) -> int:
    n = len(nums)
    # 1. Build Prefix Sum [0, n1, n1+n2, ...]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
    min_len = float('inf')
    
    # 2. For each starting point i, find the closest ending point
    for i in range(n):
        # We need: prefix_sums[?] >= target + prefix_sums[i]
        needed = target + prefix_sums[i]
        
        # Binary Search for 'needed' in the prefix_sums array
        # bisect_left returns the first index where value >= needed
        idx = bisect.bisect_left(prefix_sums, needed)
        
        # If index is within bounds, we found a valid subarray
        if idx <= n:
            min_len = min(min_len, idx - i)
            
    return 0 if min_len == float('inf') else min_len

"""


if __name__ == "__main__":
    nums = [10, 2, 3]
    target = 7
    print(min_subarray_len(target, nums))