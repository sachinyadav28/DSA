"""
**Bubble sort**
Time complexity ->
    - Best case: O(n) (When sorted array is given)
    - Worst case: O(n*2) (When unsorted array is given or
                          doing descending to ascending order)
"""


def bubble_sort(arr) -> list:
    """This function will return sorted array
    using bubble sort technique"""
    swapped = False
    # run arr (n-1) times
    for i in range(len(arr)):
        # for each step, max item will come always be at last index
        for j in range(1, len(arr)-i):
            # swap if the item is smaller then the prev item
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True

        # if we did not swapped on i=0, that means array is sorted
        if not swapped:
            break


# a = [2, 1, 69, 3, 8, 4]
# a = [1, 2, 3, 4, 5]
# a = [-1, 5, -4, 1]
# a = [2]
a = []
bubble_sort(a)
print(a)
