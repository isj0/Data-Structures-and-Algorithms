import countdown_1
import countdown_3
import factorial
import filesystem1
import filesystem2
import filesystem3
import exercise_1
import exercise_2
import solution_3
import solution_4


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Countdown 1
print("Countdown 1")
countdown_1.countdown(10)
print("")

# Countdown 2 skipped because it's infinite recursion

# Countdown 3
print("Countdown 3")
countdown_3.countdown(10)
print("")

# Factorial
print("Factorial")
assert_equal(factorial.factorial(5), 120)
assert_equal(factorial.factorial(1), 1)
assert_equal(factorial.factorial(0), 1)

# Filesystem 1
print("Filesystem 1")  # should print subdirectory_3, _2, _1
filesystem1.print_subdirectories(".")

# Filesystem 2
print("Filesystem 2")  # should also print subdirectory_1_1,  1_2, 2_1
filesystem2.print_subdirectories(".")

# Filesystem 3
print("Filesystem 3")  # should also print 2_1_1 and 2_1_2
filesystem3.print_subdirectories(".")

# Exercise 1
print("Exercise 1")
exercise_1.print_every_other(0, 10)  # should print 0 to 10

# Exercise 2
print("Exercise 2")
assert_equal(exercise_2.factorial(9), 945)

# Solution 3
print("Solution 3")
assert_equal(solution_3.sum(1, 10), 55)
assert_equal(solution_3.sum(1, 2), 3)

# Solution 4
print("Solution 4")  # Should print 1 to 33
array = [1, 2, 3,
         [4, 5, 6], 7,
         [8, [9, 10, 11, [12, 13, 14]]],
         [15, 16, 17, 18, 19, [20, 21, 22,
          [23, 24, 25, [26, 27, 29]], 30, 31], 32], 33]

solution_4.print_all_items(array)
