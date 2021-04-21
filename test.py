import bbsort
import insertionSort

unsorted_1 = [8, 5, 3, 2, 7, 6, 1, 9, 4]
sorted_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert bbsort.sort(unsorted_1) == sorted_1, "bbsort doesnt work"
