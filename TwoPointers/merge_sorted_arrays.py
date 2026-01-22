from typing import List


"""
https://leetcode.com/problems/merge-sorted-array/description/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


"""

# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     result = []
#     i, j = 0, 0
#     while i < m and j < n :
#         if nums1[i] <= nums2[j]:
#             result.append(nums1[i])
#             i += 1
#
#         else:
#             result.append(nums2[j])
#             j += 1
#
#     while i < m:
#         result.append(nums1[i])
#         i += 1
#
#     while j < n:
#         result.append(nums2[j])
#         j += 1
#
#     for index, val in enumerate(result):
#         nums1[index] = val


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = m - 1, n - 1
    place = m + n - 1

    while i >=0 and j >=0 and place >= 0:
        if nums1[i] > nums2[j]:
            nums1[place] = nums1[i]
            i -= 1

        else:
            nums1[place] = nums2[j]
            j -= 1

        place -= 1

    while i >= 0 and place >= 0:
        nums1[place] = nums1[i]
        i -= 1
        place -= 1

    while j >= 0 and place >= 0:
        nums1[place] = nums2[j]
        j -= 1
        place -= 1





if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0, 0]
    nums2 = [1, 2, 5, 6]

    print(nums1)

    merge(nums1, 3, nums2, 3)

    print(nums1)