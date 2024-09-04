# """***** 1D Array ****"""

"""
Different alogrithms for finding peak
"""

def straight_forward_algo(arr):
    """
    Straight Forward Algorithm for finding peak
    ** Time complexity - Theta(n)
    """
    for i, _ in enumerate(arr):
        if i < len(arr) - 2 and arr[i+1] >= arr[i] and arr[i+1] >= arr[i+2]:
            return arr[i+1]


def divide_conquer(arr):
    """
    Divide and Conquer Algorithm for finding peak
    """
    def find_peak_util(arr, low, high):
        mid = (low + high)//2
        # if mid is peak element
        if (mid == 0 or arr[mid-1] <= arr[mid]) and \
                (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        # If left neighbor is greater, then there must be a peak on the left side
        if mid > 0 and arr[mid] < arr[mid - 1]:
            find_peak_util(arr, low, mid - 1)
        # right neighbor is greater, then peak is on left
        return find_peak_util(arr, mid + 1, high)

    return find_peak_util(arr, 0, len(arr) - 1)


arri = [11, 3, 1, 2, 4]
print(divide_conquer(arri))
