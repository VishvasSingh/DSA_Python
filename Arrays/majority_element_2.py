from typing import List

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

https://leetcode.com/problems/majority-element-ii/
"""


def majority_elements(nums: List[int]) -> List[int]:

    # Brute force approach - using a dictionary/hashmap
    # O(N) time and space complexity
    #
    # mapping = dict()
    # for each_num in nums:
    #     if each_num in mapping:
    #         mapping[each_num] += 1
    #     else:
    #         mapping[each_num] = 1
    #
    # majority_elements_list = [each_num for each_num, count in mapping.items() if count > len(nums)//3]
    #
    # return majority_elements_list

    """
    The approach behind this solution is that there can be max two numbers that meet the criteria of occurring
    more than n/3 times in an array.
    We'll iterate through the array just once, maintaining two candidate numbers (candidate1, candidate2) and
    their respective counts (count1, count2).

    For each number num in the array, we follow these rules:

    If num is the same as candidate1, we increment count1.

    Else if num is the same as candidate2, we increment count2.

    Else if count1 is 0, we set candidate1 = num and count1 = 1.

    Else if count2 is 0, we set candidate2 = num and count2 = 1.

    Other-wise (if num is different from both candidates and both counts are non-zero),
    we decrement both count1 and count2.

    This fifth step is the key. When we see three different numbers (the current num, candidate1, and candidate2),
    they effectively cancel each other out. A true majority element will survive this process
    because it will appear more often than it gets canceled out.

    Pass 2: Verify the candidates.
    The first pass only gives us two potential candidates. It doesn't guarantee they appear more than n/3 times.
    So, we must iterate through the array a second time to count the actual occurrences of candidate1 and candidate2
    and see if they meet the > n/3 threshold.

    """

    if not nums:
        return []

        # Pass 1: Find candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Pass 2: Verify candidates
    result = []
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:  # Use elif to avoid double-counting if candidates are the same
            count2 += 1

    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result


if __name__ == "__main__":
    nums = [1,1,2,3,4,1,1,5,6,7,1,1,8,9,10,1,11,12,13,14]
    print(majority_elements(nums))