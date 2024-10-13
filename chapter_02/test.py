import linear_search
import binary_search


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


assert_equal(linear_search.linear_search([2, 5, 8, 9, 100], 8), 2)
assert_equal(linear_search.linear_search([5, 2, 8, 100, 9], 8), 2)

assert_equal(binary_search.binary_search([2, 5, 8, 9, 100], 8), 2)
assert_equal(binary_search.binary_search([2, 5, 8, 9, 100], 2), 0)
assert_equal(binary_search.binary_search([2, 5, 8, 9, 100, 101], 8), 2)
assert_equal(binary_search.binary_search([2, 5, 8, 9, 100, 101], 2), 0)
assert_equal(binary_search.binary_search([2, 5, 8, 9, 100, 101], 101), 5)
assert_equal(binary_search.binary_search(
    [-3, -1, 2, 5, 8, 9, 100, 101], 100), 6)
