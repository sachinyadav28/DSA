"""
Program for merge sort (kind of divide and conquer)
"""


def merge(arr, start, end):
    mid = (start+end)//2
    len_1 = mid - start + 1
    len_2 = end - mid

    first_arr = arr[start:mid+1]
    second_arr = arr[mid+1:end+1]

    i, j, k = 0, 0, start
    while i < len_1 and j < len_2:
        if first_arr[i] < second_arr[j]:
            arr[k] = first_arr[i]
            i += 1
        else:
            arr[k] = second_arr[j]
            j += 1
        k += 1

    while i < len_1:
        arr[k] = first_arr[i]
        i += 1
        k += 1

    while j < len_2:
        arr[k] = second_arr[j]
        j += 1
        k += 1

    del first_arr
    del second_arr


def merge_sort(arr, start, end):
    if start >= end:
        return arr
    mid = (start + end) // 2
    # left part
    merge_sort(arr, start, mid)
    # right part
    merge_sort(arr, mid+1, end)
    merge(arr, start, end)


a = [2, 1, 5, 7, 4, 3, 1, 3, 6, 4, 2, 11, 66, 33, 54, 23]
merge_sort(a, 0, len(a) - 1)
print(a)
