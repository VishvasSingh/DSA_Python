from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""

def product_except_self(nums: List[int]) -> List[int]:
    # answer = []
    # curr_left_product = 1
    # for i in range(len(nums)):
    #     if i == 0:
    #         answer.append(curr_left_product)
    #     else:
    #         curr_left_product *= nums[i-1]
    #         answer.append(curr_left_product)
    #
    # curr_right_product = 1
    # for i in range(len(nums)-1, -1, -1):
    #     if i != len(nums)-1:
    #         curr_right_product *= nums[i+1]
    #
    #     answer[i] = answer[i] * curr_right_product
    #
    # return answer

    """ The above solutions is correct, but a bit messy, a cleaner way to write it is below
        In a production environment (or a strict interview), we try to avoid conditional checks inside
        loops if the logic can be streamlined. It makes the code faster (fewer branch instructions) and easier to read.

    """
    n = len(nums)
    answer = [1] * n  # Initialize with 1s

    # Left Pass
    curr_left = 1
    for i in range(n):
        answer[i] = curr_left
        curr_left *= nums[i]  # Update for the NEXT iteration

    # Right Pass
    curr_right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= curr_right
        curr_right *= nums[i]  # Update for the NEXT iteration

    return answer






if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = product_except_self(nums)
    print(result)
