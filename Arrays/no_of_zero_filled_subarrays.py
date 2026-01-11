from typing import List

"""

https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

"""

"""
Brute force approach:

For each zero, start iterating forward and increase count by one for a consecutive zero

"""

# def zero_filled_subarrays(nums: List[int]) -> int:
#     subarrays_count = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             for j in range(i, len(nums)):
#                 if nums[j] == 0:
#                     subarrays_count += 1
#                 else:
#                     break
#
#     return subarrays_count


"""
Optimized approach:

Maintain a streak count, and add the streak count to the total, 
eg. 
for 3 consecutive zeroes, [0, 0, 0] -> the subarrays are [0], [0], [0, 0], [0, 0], [0, 0, 0]
so there are 6 subarrays in total. 
If we iterate and maintain a streak count, for the first zero, the streak count will be 1,
for the second consecutive zero, streak count will be 2,
for the third consecutive zero, streak count will be 3,
so we sum up, 1+2+3 = 6, likewise we will get our subarray count in O(N) time and O(1) space.

"""

def zero_filled_subarrays(nums: List[int]) -> int:
    streak_count = 0
    subarray_count = 0

    for i in range(0, len(nums)):
        if nums[i] == 0:
            streak_count += 1
            subarray_count += streak_count

        else:
            streak_count = 0

    return subarray_count




if __name__ == "__main__":
    nums = [0,0,0,2,0,0]
    print(zero_filled_subarrays(nums))