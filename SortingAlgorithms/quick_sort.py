from typing import List

"""
The algorithm follows these three main steps:

Pick a Pivot: First, you select an element from the array to be the "pivot." 
The choice of pivot can be done in various ways (e.g., first element, last element, median, or a random element). 
The last element is a common and simple choice.

Partition: The core of the algorithm is the partitioning step. 
You rearrange the array so that all elements smaller than the pivot are moved to its left, 
and all elements greater than the pivot are moved to its right. The pivot element is now in its final sorted position.

Recurse: After partitioning, the array is divided into two sub-arrays. 
You then recursively apply the Quick Sort algorithm to the sub-array of elements smaller 
than the pivot and the sub-array of elements larger than the pivot. 
This process continues until the sub-arrays have zero or one element, at which point they are inherently sorted.
"""


def partition(unsorted_list: List[int], low: int, high: int) -> int:
    """
    This function takes the last element as a pivot, places the pivot element
    at its correct position in the sorted array, and places all smaller
    (smaller than pivot) to left of pivot and all greater elements to right
    of pivot.

    :param unsorted_list: The list to be sorted.
    :param low: The starting index of the sub-array.
    :param high: The ending index of the sub-array.
    :return: The index of the pivot after partitioning.

    """

    pivot = unsorted_list[high]

    i = low - 1

    for j in range(low, high):
        if unsorted_list[j] <= pivot:
            i += 1
            unsorted_list[j], unsorted_list[i] = unsorted_list[i], unsorted_list[j]

    unsorted_list[i+1], unsorted_list[high] = unsorted_list[high], unsorted_list[i+1]

    return i+1


def quick_sort(unsorted_list: List[int], low: int, high: int):
    if low < high:
        pivot = partition(unsorted_list, low, high)
        quick_sort(unsorted_list, low, pivot-1)
        quick_sort(unsorted_list, pivot+1, high)


if __name__ == "__main__":
    unsorted_array = [5, 3, 6, 2, 7, 4, 7]
    print(f"Unsorted array -> {unsorted_array}")
    quick_sort(unsorted_array, 0, len(unsorted_array)-1)
    print(f"Sorted array -> {unsorted_array}")