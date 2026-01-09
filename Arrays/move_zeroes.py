from typing import List

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/

"""


def move_zeroes(nums: List[int]) -> None:
    # i, j = 0, 0
    #
    # while i < len(nums)-1 and j < len(nums)-1:
    #     while j < len(nums)-1:
    #         if nums[j] == 0:
    #             j += 1
    #         else:
    #             break
    #
    #     while i < len(nums)-1:
    #         if nums[i] != 0:
    #             i += 1
    #         else:
    #             break
    #
    #     if i < j:
    #         nums[i], nums[j] = nums[j], nums[i]
    #
    #     else:
    #         j = i

    

    """
    optimal solution: 
    count the number of swaps required and then make the last k elements 0
    
    n=len(nums)
        k=0
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for j in range(k,n):
            nums[j]=0
    """

    non_zero_itr, zero_itr = 0, 0
    for i in range(0, len(nums)+1):
        if non_zero_itr >= len(nums):
            break

        if nums[zero_itr]==0 and nums[non_zero_itr]!=0:
            nums[zero_itr], nums[non_zero_itr] = nums[non_zero_itr], nums[zero_itr]
            zero_itr+=1
            non_zero_itr+=1

        elif nums[zero_itr]!=0:
            zero_itr+=1
            non_zero_itr +=1

        else:
            non_zero_itr+=1





if __name__ == "__main__":
    nums = [0 , 0 , 2, 0, 1, 0, 1, 0 ,12 ,1 ,5 ,6 , 8 , 5 , 6 , 0 ,0 , 0, 2 , 5]
    # nums = [1, 2, 0, 4]
    print(f"Original array -> {nums}")
    move_zeroes(nums)
    print(f"Modified array -> {nums}")