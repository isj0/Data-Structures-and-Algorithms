import double_array
import factorial1
import factorial2
import array_sum
import reverse
import countx1
import countx2
import staircase1
import staircase2
import anagrams
import solution1
import solution2
import solution3
import solution4
import solution5


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Double array
print("Double array")
array = [1, 2, 3, 4, 5]
double_array.double_array(array)
assert_equal(array, [2, 4, 6, 8, 10])

# Factorial 1
print("Factorial 1")
assert_equal(factorial1.factorial(6), 720)

# Factorial 2
print("Factorial 2")
assert_equal(factorial2.factorial(6), 720)

# Array sum
print("Array sum")
assert_equal(array_sum.sum([1, 2, 3, 4, 5]), 15)
assert_equal(array_sum.sum([1]), 1)
assert_equal(array_sum.sum([]), 0)

# Reverse string
print("Reverse string")
assert_equal(reverse.reverse("abcde"), "edcba")
assert_equal(reverse.reverse("a"), "a")
# assert_equal(reverse.reverse(""), "")

# Count X 1  - Purposely not testing empty string
print("Count x 1")
assert_equal(countx1.count_x("fxsgxaxr"), 3)
assert_equal(countx1.count_x("fxsgxar"), 2)
assert_equal(countx1.count_x("fsgar"), 0)
assert_equal(countx1.count_x("x"), 1)

# Count x 2
print("Count x 2")
assert_equal(countx2.count_x("fxsgxaxr"), 3)
assert_equal(countx2.count_x("fxsgxar"), 2)
assert_equal(countx2.count_x("fsgar"), 0)
assert_equal(countx2.count_x("x"), 1)
assert_equal(countx2.count_x(""), 0)

# Staircase 1
print("Staircase 1")
assert_equal(staircase1.number_of_paths(0), 0)
assert_equal(staircase1.number_of_paths(1), 1)
assert_equal(staircase1.number_of_paths(2), 2)
assert_equal(staircase1.number_of_paths(3), 4)
assert_equal(staircase1.number_of_paths(4), 7)

# Staircase 2   = the case of 0 should return 1 because it's "rigged"
print("Staircase 2")
assert_equal(staircase2.number_of_paths(0), 1)
assert_equal(staircase2.number_of_paths(1), 1)
assert_equal(staircase2.number_of_paths(2), 2)
assert_equal(staircase2.number_of_paths(3), 4)
assert_equal(staircase2.number_of_paths(4), 7)

# Anagrams
print("Anagrams")
array = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
assert_equal(anagrams.anagrams_of("abc"), array)

# Solution 1
print("Solution 1")
assert_equal(solution1.character_count(["ab", "c", "def", "ghij"]), 10)

# Solution 2
print("Solution 2")
assert_equal(solution2.select_even([1, 2, 3, 7, 8, 0]), [2, 8, 0])

# Solution 3
print("Solution 3")
assert_equal(solution3.triangle(7), 28)

# Solution 4
print("Solution 4")
assert_equal(solution4.index_of_x("abcdefghijklmnopqrstuvwxyz"), 23)

# Solution 5
print("Solution 5")
assert_equal(solution5.unique_paths(3, 7), 28)
