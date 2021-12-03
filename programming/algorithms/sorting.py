import copy
import time

from typing import List, Optional

import numpy as np


def bubble_sort(item: List[int]) -> List[int]:
    item = copy.deepcopy(item)
    swaps = 999999
    while swaps != 0:
        swaps = 0
        for i in range(len(item) - 1):
            if item[i] > item[i + 1]:
                item[i], item[i + 1] = item[i + 1], item[i]
                swaps += 1
    return item


def insertion_sort(item: List[int]) -> List[int]:
    item = copy.deepcopy(item)
    for idx, i in enumerate(item[1:]):
        compare = idx
        while i < item[compare]:
            compare -= 1
            if compare <= 0:
                break
        if compare != idx:
            item.insert(compare + 1, item.pop(idx + 1))
    return item


def selection_sort(item: List[int]) -> List[int]:
    temp_item = copy.deepcopy(item)
    temp = list()
    for _ in range(0, len(temp_item)):
        min_item = min(temp_item)
        idx = temp_item.index(min_item)
        temp_item.pop(idx)
        temp.append(min_item)

    return temp


def merge_sort(item: List[int]) -> List[int]:
    if len(item) > 1:
        half = len(item) // 2
        split1, split2 = item[:half], item[half:]
        merged1, merged2 = merge_sort(split1), merge_sort(split2)
        temp = list()
        i = 0
        k = 0
        while (i < len(merged1)) and (k < len(merged2)):
            if merged1[i] < merged2[k]:
                temp.append(merged1[i])
                i += 1
            else:
                temp.append(merged2[k])
                k += 1

        if i == len(merged1):
            temp.extend(merged2[k:])
        else:
            temp.extend(merged1[i:])

        return temp

    else:
        return item


def quick_sort(
    item: List[int], low: Optional[int] = None, high: Optional[int] = None
) -> List[int]:
    if low is None:
        low = 0
    if high is None:
        high = len(item) - 1
    if low >= 0 and high >= 0 and low < high:
        partition_point = get_partition(item, low, high)
        quick_sort(item, low, partition_point - 1)
        quick_sort(item, partition_point + 1, high)


def get_partition(array, start, end):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end

if __name__ == "__main__":
    test = np.random.choice(a=200_000, size=20000, replace=False).tolist()
    print("Bubble sort: ")
    start = time.time()
    bubble_sort(test)
    end = time.time()
    print(f"Timing: {end - start:.2f} seconds...")
    print()

    print("Insertion sort: ")
    start = time.time()
    insertion_sort(test)
    end = time.time()
    print(f"Timing: {end - start:.2f} seconds...")
    print()

    print("Selection sort: ")
    start = time.time()
    selection_sort(test)
    end = time.time()
    print(f"Timing: {end - start:.2f} seconds...")
    print()

    print("Merge sort:")
    start = time.time()
    merge_sort(test)
    end = time.time()
    print(f"Timing: {end - start:.2f} seconds...")
    print()

    print("Quick sort:")
    test_quick_sort = copy.deepcopy(test)
    start = time.time()
    quick_sort(test)
    end = time.time()
    print(f"Timing: {end - start:.2f} seconds...")
    print()
