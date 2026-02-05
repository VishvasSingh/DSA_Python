from typing import List

"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

"""
Optimized approach:
Time complexity: O(N)
At every element of array, we have an option, either to continue adding to the curr_sum or start a new sum 

This is also known as Kadane's Algorithm.

"""

def maximum_subarray(nums: List[int]) -> int:
    max_sum, curr_sum = float('-inf'), float('-inf')

    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

"""
Greedy approach:
Time complexity: O(N logN)

The max subarray is entirely in the Left Half.

The max subarray is entirely in the Right Half.

The max subarray crosses the midpoint (starts in the left, ends in the right).

The first two are solved recursively. The third case—the Crossing Sum—is the tricky part.

To find the max subarray that strictly crosses the midpoint, you need to find:

The best sum starting at mid and expanding to the left.

The best sum starting at mid + 1 and expanding to the right.

Then add them together.


Step 1: The 'Crossing Sum' Helper

This is the only non-recursive part. Imagine you are forced to include the middle elements.

You start at the middle and walk left, keeping track of the best running sum you see.

You start at the middle and walk right, keeping track of the best running sum you see.

The total crossing sum is simply Best Left Sum + Best Right Sum.

Visual: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ] Midpoint is at index 4 (value -1).

Left part: Start at -1, go left -> 4 -> -3... find the max cumulative sum.

Right part: Start at 2, go right -> 1 -> -5... find the max cumulative sum.

Step 2: The Main Recursion
The main function simply says:

Base Case: If the array has 1 element, that element is the sum.

Recursive Step:

Solve for Left Half.

Solve for Right Half.

Solve for Crossing Sum (using the helper above).

Return: max(left_best, right_best, cross_best).

"""


def max_subarray(nums: List[int]) -> int:
    # Helper function to find maximum crossing sum
    def max_crossing_sum(left: int, mid: int, right: int) -> int:
        # 1. Include elements on left of mid
        sum_left = 0
        max_left = float('-inf')
        # Iterate backwards from mid to left
        for i in range(mid, left - 1, -1):
            sum_left += nums[i]
            max_left = max(max_left, sum_left)

        # 2. Include elements on right of mid
        sum_right = 0
        max_right = float('-inf')
        # Iterate forwards from mid + 1 to right
        for i in range(mid + 1, right + 1):
            sum_right += nums[i]
            max_right = max(max_right, sum_right)

        # Return the combined sum
        return max_left + max_right

    # Main recursive function
    def solve(left: int, right: int) -> int:
        # Base case: only one element
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        # Recursive calls
        left_max = solve(left, mid)
        right_max = solve(mid + 1, right)
        cross_max = max_crossing_sum(left, mid, right)

        return max(left_max, right_max, cross_max)

    # Initial call covering the whole array
    return solve(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    # print(maximum_subarray(nums))
    max_subarray(nums)
