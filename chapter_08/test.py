import status_codes1
import status_codes2
import subset1
import subset2
import solution1
import solution2
import solution3
import solution4


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Status Codes 1
print("Status codes 1")
assert_equal(status_codes1.status_code_meaning(200), "OK")
assert_equal(status_codes1.status_code_meaning(301), "Moved Permanently")
assert_equal(status_codes1.status_code_meaning(401, ), "Unauthorized")
assert_equal(status_codes1.status_code_meaning(404), "Not Found")
assert_equal(status_codes1.status_code_meaning(500), "Internal Server Error")

# Status Codes 2
print("Status codes 2")
assert_equal(status_codes2.status_code_meaning(200), "OK")
assert_equal(status_codes2.status_code_meaning(301), "Moved Permanently")
assert_equal(status_codes2.status_code_meaning(401, ), "Unauthorized")
assert_equal(status_codes2.status_code_meaning(404), "Not Found")
assert_equal(status_codes2.status_code_meaning(500), "Internal Server Error")

# Subset 1
print("Subset 1")
array1 = ["a", "b", "c", "d", "e", "f"]
array2 = ["b", "d", "f"]
assert_equal(subset1.is_subset(array1, array2), True)
array2 = ["b", "d", "h"]
assert_equal(subset1.is_subset(array1, array2), False)
assert_equal(subset1.is_subset([], []), True)
assert_equal(subset1.is_subset(["a"], ["b", "a"]), True)

# Subset 2
print("Subset 2")
array1 = ["a", "b", "c", "d", "e", "f"]
array2 = ["b", "d", "f"]
assert_equal(subset2.is_subset(array1, array2), True)
array2 = ["b", "d", "h"]
assert_equal(subset2.is_subset(array1, array2), False)
assert_equal(subset2.is_subset([], []), True)
assert_equal(subset2.is_subset(["a"], ["b", "a"]), True)

# Solution 1
print("Solution 1")
assert_equal(solution1.get_intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]), [2, 4])
assert_equal(solution1.get_intersection([], []), [])
assert_equal(solution1.get_intersection([1], [2]), [])

# Solution 2
print("Solution 2")
assert_equal(solution2.find_duplicate(["a", "b", "c", "d", "c", "e", "f"]), "c")
assert_equal(solution2.find_duplicate(["a", "b", "c", "d", "e", "f"]), None)
assert_equal(solution2.find_duplicate([]), None)

# Solution 3
print("Solution 3")
string = "the quick brown box jumps over a lazy dog"
assert_equal(solution3.find_missing_letter(string), "f")
string = "the quick brown fox jumps over a lazy dog"
assert_equal(solution3.find_missing_letter(string), None)

# Solution 4
print("Solution 4")
assert_equal(solution4.first_non_duplicate("minimum"), "n")
assert_equal(solution4.first_non_duplicate("llamma"), None)
