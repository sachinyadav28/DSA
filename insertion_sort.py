"""
**Insertion sort**
Time complexity ->
    - Best case: O(n) (When sorted array is given)
    - Worst case: O(n*2) (When unsorted array is given)
"""


def insertion_sort(arr):
    """
    This function will return sorted array by insertion sort technique
    by sorting array at each pass till index i+1
    """
    size = len(arr)
    for i in range(size - 1):
        # run loop in range of i+1 in decrement order
        for j in range(i + 1, 0, -1):
            # swap if prev element is smaller else break as it is sorted
            if j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


# a = [2, 1, 69, 3, 8, 4]
# a = [1, 2, 3, 4, 5]
# a = [-1, 5, -4, 1]
# a = [2]
a = []
insertion_sort(a)
print(a)
