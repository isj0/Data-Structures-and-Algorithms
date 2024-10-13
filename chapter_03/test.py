import print_list
import prime
import leap_year
import array_sum
import chessboard
import astrings
import median


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Prime numbers
print("Prime Numbers")
assert_equal(prime.is_prime(1), True)
assert_equal(prime.is_prime(2), True)
assert_equal(prime.is_prime(3), True)
assert_equal(prime.is_prime(4), False)
assert_equal(prime.is_prime(5), True)
assert_equal(prime.is_prime(6), False)
assert_equal(prime.is_prime(7), True)
assert_equal(prime.is_prime(8), False)

# Leap year
print("Leap Year")
assert_equal(leap_year.is_leap_year(1900), True)
assert_equal(leap_year.is_leap_year(1901), False)
assert_equal(leap_year.is_leap_year(1902), False)
assert_equal(leap_year.is_leap_year(1903), False)
assert_equal(leap_year.is_leap_year(1904), True)
assert_equal(leap_year.is_leap_year(2000), False)
assert_equal(leap_year.is_leap_year(2004), True)

# Array sum
print("Array sum")
assert_equal(array_sum.array_sum([3, 6, 9, 1, 8]), sum([3, 6, 9, 1, 8]))
assert_equal(array_sum.array_sum([]), 0)

# Chessboard
print("Chessboard")
assert_equal(chessboard.chessboard_space(16), 5)
assert_equal(chessboard.chessboard_space(65), 8)

# Select 'A' strings
print("A strings")
array = ['apple', 'banana', 'ant', 'aardvark', 'panda']
assert_equal(astrings.select_a_strings(array), ['apple', 'ant', 'aardvark'])
assert_equal(astrings.select_a_strings([]), [])

# Median
print("Median")
assert_equal(median.median([1, 3, 7, 9, 13]), 7)
assert_equal(median.median([1, 3, 7, 9, 13, 18]), 8)
assert_equal(median.median([1]), 1)
assert_equal(median.median([1, 2]), 1.5)
assert_equal(median.median([]), None)
