from typing import List

"""
https://leetcode.com/problems/number-of-good-pairs/description/

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


"""

"""
[1, 1, 1, 1, 1, 1] - len(6)
: 5 + 4 + 3 + 2 + 1 = 15

[1, 1, 1, 1, 1] - len(5)
: 4 + 3 + 2 + 1 = 10

[1, 1, 1, 1] - len(4)
: 3 + 2 + 1 = 6

(n * (n-1)) // 2

"""


def num_identical_pairs(nums: List[int]) -> int:
    numbers_count = {}
    total_pairs = 0
    for num in nums:
        numbers_count[num] = numbers_count.get(num, 0) + 1

    for count in numbers_count.values():
        if count > 1:
            total_pairs += (count * (count-1))//2


    return total_pairs


if __name__ == "__main__":
    nums = [1,2,3]
    print(num_identical_pairs(nums))