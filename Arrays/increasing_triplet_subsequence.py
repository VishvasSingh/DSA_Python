from typing import List

"""
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

"""

"""
Brute Force:
Fix one number and then iterate forwards and count if there are 2 elements greater than the current number.

"""

# def increasing_triplet(nums: List[int]) -> bool:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[j] > nums[i]:
#                 for k in range(j+1, len(nums)):
#                     if nums[k] > nums[j]:
#                         return True
#
#     return False


"""
Optimized Approach: O(n) time and O(1) space

We want to find a sequence Small < Medium < Large. We only need to track the smallest number found so far (first) and the second smallest number found so far (second).

The Logic: Initialize first = Infinity, second = Infinity. Iterate through every number n in the array:

Is n better than first? If n <= first, update first = n. (We found a new, lower starting point. This is good!)

Is n better than second? Else if n <= second, update second = n. (We found a number bigger than first, but smaller than the old second. This makes it easier to find a third number later!)

Is n bigger than second? Else... wait, if it's not smaller than first AND not smaller than second, it must be bigger than both! (We found first < second < n. Return True!)

Why this works (The Tricky Part): Consider [3, 5, 1, 6].

n=3: first becomes 3.

n=5: 5 > 3, so second becomes 5. (We have a potential sequence starting with 3, 5).

n=1: 1 < 3, so first becomes 1.

Wait! Does this break our 3, 5 pair? No. second is still 5. The fact that second is 5 implies there was a number before it (3) that was smaller.

If we find a number bigger than 5 later, we are done.

n=6: 6 > 5. We return True. (The triplet is 3, 5, 6).

"""


def increasing_triplet(nums: List[int]) -> bool:
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num  # Found a smaller 'first' candidate
        elif num <= second:
            second = num  # Found a smaller 'second' candidate
        else:
            # If we reach here, num is > first AND num > second
            return True

    return False




if __name__ == "__main__":
    nums = [2,1,5,0,4,6]
    print(increasing_triplet(nums))