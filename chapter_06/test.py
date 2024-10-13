import insertion_sort
import intersection1
import intersection2
import two_sum
import contains_x
import contains_x_solution


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Insertion Sort
print("Insertion Sort")
assert_equal(insertion_sort.insertion_sort([]), [])
assert_equal(insertion_sort.insertion_sort([5]), [5])
assert_equal(insertion_sort.insertion_sort([1, 5]), [1, 5])
assert_equal(insertion_sort.insertion_sort([5, 1]), [1, 5])
assert_equal(insertion_sort.insertion_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
assert_equal(insertion_sort.insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
array = [1, 9, 3, 4, 5, 10, 0]
assert_equal(insertion_sort.insertion_sort(array), [0, 1, 3, 4, 5, 9, 10])

# Intersecton 1
print("Intersecton 1")
assert_equal(intersection1.intersection([3, 1, 4, 2], [4, 5, 3, 6]), [3, 4])
assert_equal(intersection1.intersection([3, 1, 4, 2], [5, 3, 6]), [3])
assert_equal(intersection1.intersection([], []), [])
assert_equal(intersection1.intersection([], [1]), [])
assert_equal(intersection1.intersection([1], []), [])
assert_equal(intersection1.intersection([1, 2, 3], [4, 5, 6]), [])

# Intersecton 2
print("Intersecton 2")
assert_equal(intersection2.intersection([3, 1, 4, 2], [4, 5, 3, 6]), [3, 4])
assert_equal(intersection2.intersection([3, 1, 4, 2], [5, 3, 6]), [3])
assert_equal(intersection2.intersection([], []), [])
assert_equal(intersection2.intersection([], [1]), [])
assert_equal(intersection2.intersection([1], []), [])
assert_equal(intersection2.intersection([1, 2, 3], [4, 5, 6]), [])

# Two Sum
print("Two Sum")
assert_equal(two_sum.two_sum([]), False)
assert_equal(two_sum.two_sum([1]), False)
assert_equal(two_sum.two_sum([1, 2, 3, 10]), False)
assert_equal(two_sum.two_sum([1, 2, 3, 4]), False)
assert_equal(two_sum.two_sum([1, 2, 3, 8]), True)
assert_equal(two_sum.two_sum([1, 2, 3, 9]), True)

# Contains X - Exercise
print("Contains X - Exercise")
assert_equal(contains_x.contains_X(""), False)
assert_equal(contains_x.contains_X(" "), False)
assert_equal(contains_x.contains_X("ABCDx"), False)
assert_equal(contains_x.contains_X("xxxxx"), False)
assert_equal(contains_x.contains_X("X"), True)
assert_equal(contains_x.contains_X("ADSFXPODFO"), True)

# Contains X - Solution
print("Contains X - Solution")
assert_equal(contains_x_solution.contains_X(""), False)
assert_equal(contains_x_solution.contains_X(" "), False)
assert_equal(contains_x_solution.contains_X("ABCDx"), False)
assert_equal(contains_x_solution.contains_X("xxxxx"), False)
assert_equal(contains_x_solution.contains_X("X"), True)
assert_equal(contains_x_solution.contains_X("ADSFXPODFO"), True)
