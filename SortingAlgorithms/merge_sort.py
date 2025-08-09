from typing import List

"""
This is divide and conquer type of algorithm, where we divide the array into two sorted halves and then merge them into
one while comparing elements from both the sorted arrays. Now to divide them into sorted halves, we keep dividing the 
main array until there is only one element left, since an array of one element is sorted, we start merging until we have
arrived at the sorted array
"""


def merge_sort(unsorted_array: List[int]) -> None:
    if len(unsorted_array) > 1:
        mid = len(unsorted_array)//2
        left = unsorted_array[:mid]
        right = unsorted_array[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
                k += 1

            else:
                unsorted_array[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    unsorted_array = [5, 3, 6, 2, 7, 4, 7]
    print(f"Unsorted array -> {unsorted_array}")
    merge_sort(unsorted_array)
    print(f"Sorted array -> {unsorted_array}")