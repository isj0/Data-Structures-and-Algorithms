import array_max1
import array_max2
import fib1
import fib2
import fib3
import exercise1
import exercise2
import exercise3
import solution1
import solution2
import solution3


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Array max 1
print("Array max 1")
assert_equal(array_max1.max([4, 6, 0, 1, 3, 3, 5]), 6)
assert_equal(array_max1.max([]), None)

# Array max 2
print("Array max 2")
assert_equal(array_max2.max([4, 6, 0, 1, 3, 3, 5]), 6)
assert_equal(array_max2.max([]), None)

# Fibonacci 1
print("Fibonacci 1")
assert_equal(fib1.fib(0), 0)
assert_equal(fib1.fib(1), 1)
assert_equal(fib1.fib(2), 1)
assert_equal(fib1.fib(3), 2)
assert_equal(fib1.fib(7), 13)

# Fibonacci 2
print("Fibonacci 2")
assert_equal(fib2.fib(0, {}), 0)
assert_equal(fib2.fib(1, {}), 1)
assert_equal(fib2.fib(2, {}), 1)
assert_equal(fib2.fib(3, {}), 2)
assert_equal(fib2.fib(7, {}), 13)

# Fibonacci 2
print("Fibonacci 3")
assert_equal(fib3.fib(0), 0)
assert_equal(fib3.fib(1), 1)
assert_equal(fib3.fib(2), 1)
assert_equal(fib3.fib(3), 2)
assert_equal(fib3.fib(7), 13)

# Exercise 1
print("Exercise 1")
assert_equal(exercise1.add_until_100([3, 6, 5, 11, 90]), 98)

# Solution 1
print("Solution 1")
assert_equal(solution1.add_until_100([3, 6, 5, 11, 90]), 98)

# Exercise 2
print("Exercise 2")
assert_equal(exercise2.golomb(1), 1)
assert_equal(exercise2.golomb(2), 2)
assert_equal(exercise2.golomb(5), 3)
assert_equal(exercise2.golomb(30), 10)

# Solution 2
print("Solution 2")
assert_equal(solution2.golomb(1, {}), 1)
assert_equal(solution2.golomb(2, {}), 2)
assert_equal(solution2.golomb(5, {}), 3)
assert_equal(solution2.golomb(30, {}), 10)

# Exercise 3
print("Exercise 3")
assert_equal(exercise3.unique_paths(3, 7), 28)

# Solution 3
print("Solution 3")
assert_equal(solution3.unique_paths(3, 7, {}), 28)
