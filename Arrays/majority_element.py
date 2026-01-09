from typing import List


def majority_element(nums: List[int]) -> int:
    curr_candidate = nums[0]
    curr_candidate_count = 1

    for i in range (1, len(nums)):
        if nums[i] == curr_candidate:
            curr_candidate_count += 1
        else:
            curr_candidate_count -= 1

        if curr_candidate_count <= 0:
            curr_candidate = nums[i]
            curr_candidate_count = 1

    return curr_candidate


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majority_element(nums))