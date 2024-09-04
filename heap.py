"""
MAX_HEAPIFY
"""


def max_heapify(arr, i):
    heap_size = len(arr)
    left = 2*i+1
    right = 2*i+2
    if left <= heap_size and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right <= heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


a = [16, 12, 13, 14, 8, 10]
b = [-i for i in a]
# max_h = max_heapify(a, 2)
# print(max_h)
import heapq
heapq.heapify(b) # Min heap
print(b)
# heapq._heapify_max(a) # Max heap
