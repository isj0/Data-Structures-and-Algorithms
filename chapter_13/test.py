import sortable_array
import duplicate
import solution1
import exercise2
import solution2
import solution3a
import solution3b
import solution3c


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Partition
print("Partition")
array = sortable_array.SortableArray([7, 8, 1, 9, 0, 4])
left_pointer = array.partition(0, 5)
assert_equal(left_pointer, 2)
assert_equal(array.array, [0, 1, 4, 9, 7, 8])

# Quicksort
print("Quicksort")
array = sortable_array.SortableArray([7, 8, 1, 9, 0, 4])
array.quicksort(0, 5)
assert_equal(array.array, [0, 1, 4, 7, 8, 9])

array = sortable_array.SortableArray([12, 11, 10, 7, 8, 1, 9, 0, 4, 15, 3, 6, 5, 3, 4, 6, 7, 7, 4, 3, 2, 1, 5, 3, 3, 3])
array.quicksort(0, 25)
assert_equal(array.array, [0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 9, 10, 11, 12, 15])

array = sortable_array.SortableArray([])
array.quicksort(0, 0)
assert_equal(array.array, [])

array = sortable_array.SortableArray([5])
array.quicksort(0, 0)
assert_equal(array.array, [5])

array = sortable_array.SortableArray([5, 2])
array.quicksort(0, 1)
assert_equal(array.array, [2, 5])

# Quickselect
print("Quickselect")

array = sortable_array.SortableArray([0, 50, 20, 10, 60, 30])
assert_equal(array.quickselect(1, 0, 5), 10)

array = sortable_array.SortableArray([30])
assert_equal(array.quickselect(0, 0, 0), 30)

# Duplicate value
print("Duplicate value")
assert_equal(duplicate.has_duplicate_value([5, 9, 3, 2, 4, 5, 6]), True)
assert_equal(duplicate.has_duplicate_value([9, 3, 2, 4, 5, 6]), False)
assert_equal(duplicate.has_duplicate_value([]), False)
assert_equal(duplicate.has_duplicate_value([1]), False)

# Solution 1
print("Solution 1")
assert_equal(solution1.greatest_product_of_3([9, 3, 5, 1, 0, 4]), 180)

# Exercise 2
print("Exercise 2")
assert_equal(exercise2.find_missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4]), 8)

# Solution 2
print("Solution 2")
assert_equal(solution2.find_missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4]), 8)

# Solution 3a
print("Solution 3a")
assert_equal(solution3a.max([9, 3, 2, 5, 6, 7, 11, 0, 4]), 11)
assert_equal(solution3a.max([5]), 5)
assert_equal(solution3a.max([]), None)

# Solution 3b
print("Solution 3b")
assert_equal(solution3b.max([9, 3, 2, 5, 6, 7, 11, 0, 4]), 11)
assert_equal(solution3b.max([5]), 5)
assert_equal(solution3b.max([]), None)

# Solution 3c
print("Solution 3c")
assert_equal(solution3c.max([9, 3, 2, 5, 6, 7, 11, 0, 4]), 11)
assert_equal(solution3c.max([5]), 5)
assert_equal(solution3c.max([]), None)
