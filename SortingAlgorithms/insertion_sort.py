from typing import List

"""
The idea behind insertion sort is that we maintain a sorted array on left side, and we pick elements from right side 
and keep placing them in the sorted array at the correct place. Basically "inserting" a number at it's correct place
in a sorted array (since we start with only one element on left side, that is our sorted array in the beginning) 
we keep moving right and for each element, we check where it fits in our sorted array, we keep moving that element 
to the left until it reaches it's correct spot. 
"""


def insertion_sort(unsorted_list: List[int]) -> List[int]:
    list_length = len(unsorted_list)
    for i in range(1, list_length):
        key = unsorted_list[i]
        j = i-1

        while j >= 0 and unsorted_list[j] > key:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1

        unsorted_list[j+1] = key

    return unsorted_list


if __name__ == '__main__':
    unsorted_array = [5, 3, 6, 2, 7, 4, 7]
    print(f"Unsorted array -> {unsorted_array}")
    sorted_array = insertion_sort(unsorted_array)
    print(f"Sorted array -> {sorted_array}")


