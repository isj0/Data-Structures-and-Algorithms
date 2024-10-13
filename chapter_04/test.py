import bubble_sort
import duplicates1
import duplicates2
import duplicates3
import duplicates4
import greatest_product
import greatest_number_exercise
import solution_greatest_number


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Bubble Sort
print("Bubble Sort")
assert_equal(bubble_sort.bubble_sort([]), [])
assert_equal(bubble_sort.bubble_sort([5]), [5])
assert_equal(bubble_sort.bubble_sort([1, 5]), [1, 5])
assert_equal(bubble_sort.bubble_sort([5, 1]), [1, 5])
assert_equal(bubble_sort.bubble_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
assert_equal(bubble_sort.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
array = [1, 9, 3, 4, 5, 10, 0]
assert_equal(bubble_sort.bubble_sort(array), [0, 1, 3, 4, 5, 9, 10])

# Duplicates #1
print("Duplicates #1")
assert_equal(duplicates1.has_duplicate_value([]), False)
assert_equal(duplicates1.has_duplicate_value([1]), False)
assert_equal(duplicates1.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates1.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates1.has_duplicate_value([1, 2, 3, 4, 1]), True)

# Duplicates #2
print("Duplicates #2")
assert_equal(duplicates2.has_duplicate_value([]), False)
assert_equal(duplicates2.has_duplicate_value([1]), False)
assert_equal(duplicates2.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates2.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates2.has_duplicate_value([1, 2, 3, 4, 1]), True)

# Duplicates #3
print("Duplicates #3")
assert_equal(duplicates3.has_duplicate_value([]), False)
assert_equal(duplicates3.has_duplicate_value([1]), False)
assert_equal(duplicates3.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates3.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates3.has_duplicate_value([1, 2, 3, 4, 1]), True)
assert_equal(duplicates3.has_duplicate_value([10, 2, 3, 4, 10]), True)
assert_equal(duplicates3.has_duplicate_value([0, 2, 3, 4, 0]), True)


# Duplicates #4
print("Duplicates #4")
assert_equal(duplicates4.has_duplicate_value([]), False)
assert_equal(duplicates4.has_duplicate_value([1]), False)
assert_equal(duplicates4.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates4.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates4.has_duplicate_value([1, 2, 3, 4, 1]), True)

# Greatest Product
print("Greatest Product")
assert_equal(greatest_product.greatest_product([]), None)
assert_equal(greatest_product.greatest_product([1]), None)
assert_equal(greatest_product.greatest_product([1, 2]), 2)
assert_equal(greatest_product.greatest_product([5, 2, 4, 1]), 20)
assert_equal(greatest_product.greatest_product([5, 2, -4, 1]), 10)

# Greatest Number - Exercise
print("Greatest Number - Exercise")
assert_equal(greatest_number_exercise.greatest_number([]), None)
assert_equal(greatest_number_exercise.greatest_number([1]), 1)
assert_equal(greatest_number_exercise.greatest_number([1, 3, 5]), 5)
assert_equal(greatest_number_exercise.greatest_number([5, 3, 1]), 5)
assert_equal(greatest_number_exercise.greatest_number([5, 3, 1, 9, 7, -4]), 9)

# Greatest Number - Solution
print("Greatest Number - Solution")
assert_equal(solution_greatest_number.greatest_number([]), None)
assert_equal(solution_greatest_number.greatest_number([1]), 1)
assert_equal(solution_greatest_number.greatest_number([1, 3, 5]), 5)
assert_equal(solution_greatest_number.greatest_number([5, 3, 1]), 5)
assert_equal(solution_greatest_number.greatest_number([5, 3, 1, 9, 7, -4]), 9)
