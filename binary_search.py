"""
Binary Search programs
"""


def binary_search(arr, target):
    """
    Function for finding element in arr with O(log n)
    """
    def find_element(arr, low, high, target):
        mid = (low + high)//2

        # if mid is the element
        if arr[mid] == target:
            return mid
        # if element is at left side
        if arr[mid] > target:
            return find_element(arr, low, mid - 1, target)
        # if element is at right side
        return find_element(arr, mid + 1, high, target)

    return find_element(arr, 0, len(arr) - 1, target)


nums = [-1,0,2,4,6,8]
tar = 4
print(binary_search(nums, tar))
