#!/usr/bin/python3
"""
 a function that finds a peak in a list of unsorted integers.
"""
def find_peak(arr):
    """
     a function that finds a peak in a list of unsorted integers.
    """
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]

        # If right neighbor is greater, search right half
        elif mid < n - 1 and arr[mid + 1] > arr[mid]:
            low = mid + 1
        # Otherwise, search left half
        else:
            high = mid - 1

    return None  # No peak found
