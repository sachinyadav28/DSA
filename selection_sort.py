"""
**Bubble sort**
Time complexity ->
    - Best case: O(n*2) (When sorted array is given)
    - Worst case: O(n*2) (When unsorted array is given)
"""


def selection_sort(arr):
    """
    This function will return sorted array by selection sort technique
    by selecting maximum element from the array
    """
    size = len(arr)
    for i in range(size):
        last = size - i - 1  # last index
        max_index = get_max_index(arr, 0, last)
        # swap max element with the last element
        arr[last], arr[max_index] = arr[max_index], arr[last]


def get_max_index(arr, start, last):
    """
    Returns index of maximum element in the array
    """
    max_index = start
    for i in range(start, last + 1):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


# a = [2, 1, 69, 3, 8, 4]
# a = [1, 2, 3, 4, 5]
# a = [-1, 5, -4, 1]
a = [2]
# a = []
selection_sort(a)
print(a)
