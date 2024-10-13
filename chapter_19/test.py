import uppercase1
import uppercase2
import duplicates5
import duplicates6
import recurse
import loop
import exercise2
import solution3
import exercise4


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Uppercase 1
print("Uppercase 1")
assert_equal(uppercase1.make_uppercase(['a', 'b', 'c']), ['A', 'B', 'C'])

# Uppercase 2
print("Uppercase 2")
assert_equal(uppercase2.make_uppercase(['a', 'b', 'c']), ['A', 'B', 'C'])

# Duplicates 1 was already tested back in Chapter 4

# Duplicates 5
print("Duplicates #5")
assert_equal(duplicates5.has_duplicate_value([]), False)
assert_equal(duplicates5.has_duplicate_value([1]), False)
assert_equal(duplicates5.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates5.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates5.has_duplicate_value([1, 2, 3, 4, 1]), True)

# Duplicates 6
print("Duplicates #6")
assert_equal(duplicates6.has_duplicate_value([]), False)
assert_equal(duplicates6.has_duplicate_value([1]), False)
assert_equal(duplicates6.has_duplicate_value([1, 2, 3, 4]), False)
assert_equal(duplicates6.has_duplicate_value([1, 2, 2, 3]), True)
assert_equal(duplicates6.has_duplicate_value([1, 2, 3, 4, 1]), True)

# Recurse
print("Recurse")
recurse.recurse(5)

# Loop
print("Loop")
loop.loop(5)

# Exercise 2
print("Exercise 2")
assert_equal(exercise2.reverse([1, 3, 5, 7]), [7, 5, 3, 1])

# Solution 3
print("Solution 3")
assert_equal(solution3.reverse([1, 3, 5, 7]), [7, 5, 3, 1])
assert_equal(solution3.reverse([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])

# Exercise 4
print("Exercise 4")
assert_equal(exercise4.double_array_1([5, 4, 3, 2, 1]), [10, 8, 6, 4, 2])
assert_equal(exercise4.double_array_2([5, 4, 3, 2, 1]), [10, 8, 6, 4, 2])
assert_equal(exercise4.double_array_3([5, 4, 3, 2, 1]), [10, 8, 6, 4, 2])
