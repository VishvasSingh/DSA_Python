from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

"""
Brute force approach:
    For each element, run two nested for loops to find the pair that sums to 0
    Time Complexity: O(N^3) 

"""

"""
Optimized approach:
    1. Sort the array: O(N logN)
    2. Fix each element and find the pair with sum equal to -ve of current element, similar to two sum problem.
    3. Since the array is sorted, the duplicates will occur next to each other, if arr[left] == arr[left-1], skip it.

"""



def three_sum(nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    solutions = []
    for i in range(len(sorted_nums)):
        if 0 < i < len(nums) and sorted_nums[i] == sorted_nums[i-1]:
            # skipping duplicates
            continue

        large_ptr = len(sorted_nums) - 1
        small_ptr = i + 1
        target = -1 * sorted_nums[i]
        while small_ptr < large_ptr:
            curr_sum = sorted_nums[small_ptr] + sorted_nums[large_ptr]
            if curr_sum < target:
                small_ptr += 1

            elif curr_sum > target:
                large_ptr -= 1

            else:
                solutions.append([sorted_nums[i], sorted_nums[small_ptr], sorted_nums[large_ptr]])
                small_ptr += 1
                large_ptr -= 1

                # SKIP DUPLICATES for the second number
                while small_ptr < large_ptr and sorted_nums[small_ptr] == sorted_nums[small_ptr - 1]:
                    small_ptr += 1

    return [] if not solutions else solutions



if __name__ == "__main__":
    nums = [0,0, -1]
    print(three_sum(nums))