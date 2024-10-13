import selection_sort
import print_numbers
import double_sum
import multicase
import every_other


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Selection Sort
print("Selection Sort")
assert_equal(selection_sort.selection_sort([]), [])
assert_equal(selection_sort.selection_sort([5]), [5])
assert_equal(selection_sort.selection_sort([1, 5]), [1, 5])
assert_equal(selection_sort.selection_sort([5, 1]), [1, 5])
assert_equal(selection_sort.selection_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
assert_equal(selection_sort.selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
array = [1, 9, 3, 4, 5, 10, 0]
assert_equal(selection_sort.selection_sort(array), [0, 1, 3, 4, 5, 9, 10])

# Print numbers
print("Print numbers: Should print even numbers 2 - 10 twice")
print_numbers.print_numbers_version_one(10)
print_numbers.print_numbers_version_two(10)

# Double sum
print("Double sum")
assert_equal(double_sum.double_then_sum([]), 0)
assert_equal(double_sum.double_then_sum([1, 4, 9]), 28)

# Multiple cases
print("Multiple cases")
multicase.multiple_cases(["hElLo", "gooDbYe"])

# Every other
print("Every other - should print 2 3 4 4 5 6")
every_other.every_other([1, 2, 3])
