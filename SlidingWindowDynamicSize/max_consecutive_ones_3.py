from typing import List


"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/max-consecutive-ones-iii/description/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

"""
Brute Force approach: 
From every number start counting as long as nums[i] == 1 or k != 0 
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

"""
Optimized approach: Maintain a window, keep moving right as long as nums[i] == 1 or k>0
If k <= 0 then move the left pointer towards right, and if 0 is encountered then increase k by 1.
"""


"""
SCRATCHPAD:

[0, 0, 1, 1], K = 1

left = 0, right = 0 
k = 0, max_window = 1

left = 0, right = 1
k = -1, we increase left until 

"""


"""
Optimized O(N) solution but with complex code
"""

# def longest_ones(nums: List[int], k: int) -> int:
#     left = 0
#     max_window = 0
#
#     for right in range(len(nums)):
#         curr_val = nums[right]
#         if curr_val  == 1 or k > 0:
#             if curr_val == 0:
#                 k -= 1
#
#             max_window = max(max_window, right - left + 1)
#
#         else:
#             k -= 1
#             while k < 1 and left <= right:
#                 if nums[left] == 0:
#                     k += 1
#                     left += 1
#
#                     if left == right or (k>=0 and right+1<=len(nums)-1 and nums[right+1] != 0):
#                         break
#
#                 else:
#                     left += 1
#
#
#
#     return max_window


"""
Optimized solution: O(N) with cleaner code

While writing clean code I just thought about the solution differently, 
Instead of tracking how many zeroes can be converted to 1, I started tracking 
how many zeroes are inside the window, that helped simplify the logic a lot. 
Just thinking about the solution approach a little bit differently can reduce the need for 
many conditional checks and simplifies the code a lot.

"""

def longest_ones(nums: List[int], k: int) -> int:
    curr_window_zero_count = 0
    left = 0
    max_window_len = 0

    for right in range(len(nums)):
        if nums[right] != 1 and curr_window_zero_count <= k:
            curr_window_zero_count += 1

        while left <= right and curr_window_zero_count > k:
            if nums[left] == 0:
                curr_window_zero_count -= 1

            left += 1

        max_window_len = max(max_window_len, right-left+1)

    return max_window_len

if __name__ == "__main__":
    # nums = [0 ,0 , 1, 1]
    # k = 1
    # nums = [1,1,1,0,0,0,1,1,1,1,0]
    # k = 2
    # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    # k = 3
    # nums = [0, 0, 0, 1, 1, 1, 0 , 0, 0, 0]
    # k = 4
    # nums = [0, 0, 0, 1, 1, 1, 1]
    # k = 4
    # nums = [0,0,1,1,1,0,0]
    # k = 0
    nums = [0,0,0, 0,1]
    k = 3
    print(longest_ones(nums, k))