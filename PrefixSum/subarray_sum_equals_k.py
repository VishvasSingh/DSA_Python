from typing import List

"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

def subarray_sum(nums: List[int], k: int) -> int:
    prefix_sum = {0: 1}
    curr_sum = 0
    total_subarray_count = 0

    for num in nums:
        curr_sum += num

        if curr_sum - k in prefix_sum:
            total_subarray_count += prefix_sum.get(curr_sum-k, 0)

        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1


    return total_subarray_count




if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print(subarray_sum(nums,k))
