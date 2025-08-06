from typing import List

"""
The idea behind bubble sort is that we iterate through the array, we keep pushing larger elements to the end
The word "bubble" comes from this movement of elements to the end/top like a bubble 

"""


def bubble_sort(unsorted_list: List[int]) -> List[int]:
    list_length = len(unsorted_list)
    for i in range(list_length):
        for j in range(list_length - i - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j+1], unsorted_list[j] = unsorted_list[j], unsorted_list[j+1]

    return unsorted_list


if __name__ == '__main__':
    unsorted_array = [5, 3, 6, 2, 7, 4, 7]
    print(f"Unsorted array -> {unsorted_array}")
    sorted_array = bubble_sort(unsorted_array)
    print(f"Sorted array -> {sorted_array}")
