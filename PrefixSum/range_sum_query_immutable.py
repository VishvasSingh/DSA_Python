from typing import List


"""
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = self.calc_prefix_sum()

    def calc_prefix_sum(self) -> List[int]:
        prefix_sum = list()
        curr_prefix_sum = 0
        for index, ele in enumerate(self.nums):
            curr_prefix_sum += self.nums[index-1] if index > 0 else 0
            prefix_sum.append(curr_prefix_sum)

        return prefix_sum

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[right]



"""
Cleaner solution:

class NumArray:
    def __init__(self, nums: List[int]):
        # Size N+1. P[0] is 0.
        self.prefix_sum = [0] * (len(nums) + 1)
        
        # P[i] = Sum of nums[0...i-1]
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Sum(0...right) - Sum(0...left-1)
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

"""



if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sum_range(0,2))