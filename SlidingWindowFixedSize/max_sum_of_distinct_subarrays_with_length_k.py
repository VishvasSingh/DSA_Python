import json
from typing import List
from utils import time_it

"""
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105

"""



"""
Brute Force approach is to check for each subarray with size k and find out iteratively whether every element is unique 
in the sliding window. The time taken is O(N^2)


@time_it
def maximum_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0

    max_sum = 0
    curr_sum = 0
    curr_window = list()
    for i in range(k):
        curr_sum += nums[i]
        curr_window.append(nums[i])

    if len(curr_window) == len(set(curr_window)):
        max_sum = max(max_sum, curr_sum)

    for i in range(k, len(nums)):
        curr_sum -= nums[i - k]
        curr_sum += nums[i]
        curr_window.remove(nums[i - k])
        curr_window.append(nums[i])
        if len(curr_window) == len(set(curr_window)):
            max_sum = max(max_sum, curr_sum)

    return max_sum
"""

"""
Optimized approach: O(N) time and O(k) space

## IMPORTANT ##

The optimized approach took:
maximum_subarray_sum took 0.020766 seconds

Whereas the brute force solution took:
6.6 seconds.

This shows how important it is to choose the right data structure.

"""

@time_it
def maximum_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0

    max_sum = 0
    curr_sum = 0
    curr_window = dict()
    for i in range(k):
        curr_sum += nums[i]
        curr_window[nums[i]] = curr_window.get(nums[i], 0) + 1

    if len(curr_window) == k:
        max_sum = max(max_sum, curr_sum)

    for i in range(k, len(nums)):
        curr_sum -= nums[i - k]
        curr_sum += nums[i]
        if curr_window[nums[i - k]] == 1:
            del curr_window[nums[i - k]]
        else:
            curr_window[nums[i - k]] = curr_window.get(nums[i - k], 0) - 1

        curr_window[nums[i]] = curr_window.get(nums[i], 0) + 1
        if len(curr_window) == k:
            max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    with open("large_array.json", 'r') as file:
        json_data = json.load(file)
        nums = json_data.get("large_array")
    k = 5120
    print(maximum_subarray_sum(nums, k))
