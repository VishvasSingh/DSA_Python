from typing import List

"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.


"""


"""
    Brute force approach:
     Fix one element and iterate over the array to find another element which adds upto the target.

"""


"""
    Optimized approach:     [1, 2, 5, 6, 7, 9, 11, 13, 16, 17, 20], target = 20  correct pair (7, 13)
    
    fix one small pointer at left 
    start large pointer at right, 
    move left pointer to right if curr_sum = arr[left_pointer] + arr[right_pointer] < target
    move right pointer to left if curr_sum = arr[left_pointer] + arr[right_pointer] > target
    
    return the left pointer and right pointer pair if the sum is equal to the target.

"""

def two_sum(nums: List[int], target: int) -> List[int]:
    large_ptr = len(nums) - 1
    small_ptr = 0

    while small_ptr < large_ptr:
        curr_sum = nums[small_ptr] + nums[large_ptr]
        if curr_sum < target:
            small_ptr += 1

        elif curr_sum > target:
            large_ptr -= 1

        else:
            return [small_ptr + 1, large_ptr + 1]


    return [-1, -1]



if __name__ == "__main__":
    nums, target = [1, 2, 5, 6, 7, 9, 11, 13, 16, 17, 20], 20
    print(two_sum(nums, target))

