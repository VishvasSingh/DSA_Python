from typing import List


"""

    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""

def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    unique_element_pos_tracker = 0

    for i in range(1, len(nums)):
        if nums[unique_element_pos_tracker] != nums[i]:
            unique_element_pos_tracker += 1
            nums[unique_element_pos_tracker] = nums[i]

    return unique_element_pos_tracker + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    index = remove_duplicates_from_sorted_array(nums)
    print(index, nums)
