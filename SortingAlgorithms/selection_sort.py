from typing import List

"""
Selection sort maintains an unsorted and sorted array, we find the minimum (can be done using max also) element and 
place it at it's correct position, first the smallest element is placed at 0th index then we iterate the list again
and the second-smallest element is placed at 1st index, similarly from whatever position we are starting the iteration
again, the smallest element in unsorted array will be placed at that index 

"""


def selection_sort(unsorted_list: List[int]) -> List[int]:
    list_length = len(unsorted_list)
    for i in range(list_length):
        min_element_index = i
        for j in range(i+1, list_length):
            if unsorted_list[j] < unsorted_list[min_element_index]:
                min_element_index = j

        unsorted_list[i], unsorted_list[min_element_index] = unsorted_list[min_element_index], unsorted_list[i]

    return unsorted_list


if __name__ == '__main__':
    unsorted_array = [5, 3, 6, 2, 7, 4, 7]
    print(f"Unsorted array -> {unsorted_array}")
    sorted_array = selection_sort(unsorted_array)
    print(f"Sorted array -> {sorted_array}")