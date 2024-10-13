import average_even
import word_builder_1
import word_builder_2
import array_sample
import celsius
import labels
import count_ones
import palindrome
import products1
import products2
import password
import exercise1
import exercise2
import exercise3
import exercise4
import exercise5


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Password cracker
print("Password cracker")
password.every_password(2)

# Average of even numbers
print("Average of even numbers")
assert_equal(average_even.average_of_even_numbers([1, 2, 3, 4, 5, 6]), 4)
assert_equal(average_even.average_of_even_numbers([1, 2, 3, 4, 5, 6, 8]), 5)
assert_equal(average_even.average_of_even_numbers([]), None)
assert_equal(average_even.average_of_even_numbers([1, 3, 5]), None)

# Word Builder 1
print("Word Builder 1")
result_array = [
    'ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca',
    'cb', 'cd', 'da', 'db', 'dc']
assert_equal(word_builder_1.word_builder(['a', 'b', 'c', 'd']), result_array)
assert_equal(word_builder_1.word_builder([]), [])
assert_equal(word_builder_1.word_builder(['a']), [])

# Word Builder 2
print("Word Builder 2")
result_array = [
    'abc', 'abd', 'acb', 'acd', 'adb', 'adc', 'bac', 'bad',
    'bca', 'bcd', 'bda', 'bdc', 'cab', 'cad', 'cba', 'cbd',
    'cda', 'cdb', 'dab', 'dac', 'dba', 'dbc', 'dca', 'dcb'
    ]
assert_equal(word_builder_2.word_builder(['a', 'b', 'c', 'd']), result_array)
assert_equal(word_builder_2.word_builder([]), [])
assert_equal(word_builder_2.word_builder(['a']), [])

# Array sample
print("Array sample")
assert_equal(array_sample.sample([1, 2, 3, 4, 5]), [1, 3, 5])
assert_equal(array_sample.sample([1, 2, 3, 4]), [1, 3, 4])
assert_equal(array_sample.sample([1]), [1, 1, 1])
assert_equal(array_sample.sample([]), None)

# Average Celsius reading
print("Average Celsius reading")
assert_equal(celsius.average_celsius([20, 80, 45, 71]), 12.0)
assert_equal(celsius.average_celsius([-40]), -40.0)
assert_equal(celsius.average_celsius([]), None)

# Clothing labels
print("Clothing labels")
array = [
    "Purple Shirt Size: 1",
    "Purple Shirt Size: 2",
    "Purple Shirt Size: 3",
    "Purple Shirt Size: 4",
    "Purple Shirt Size: 5",
    "Green Shirt Size: 1",
    "Green Shirt Size: 2",
    "Green Shirt Size: 3",
    "Green Shirt Size: 4",
    "Green Shirt Size: 5"
]
assert_equal(labels.mark_inventory(["Purple Shirt", "Green Shirt"]), array)
assert_equal(labels.mark_inventory([]), [])

# Count ones
print("Count ones")
array = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0]
]
assert_equal(count_ones.count_ones(array), 7)

# Palindrome
print("Palindrome")

assert_equal(palindrome.is_palindrome(""), True)
assert_equal(palindrome.is_palindrome("car"), False)
assert_equal(palindrome.is_palindrome("o"), True)
assert_equal(palindrome.is_palindrome("oo"), True)
assert_equal(palindrome.is_palindrome("racecar"), True)

# Products 1
print("Products - Single Array")
array = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
assert_equal(products1.two_number_products([1, 2, 3, 4, 5]), array)
assert_equal(products1.two_number_products([]), [])
assert_equal(products1.two_number_products([2]), [])

# Products 2
print("Products - Double Array")
array = [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]
assert_equal(products2.two_number_products([1, 2, 3], [10, 100, 1000]), array)
assert_equal(products2.two_number_products([], []), [])
assert_equal(products2.two_number_products([1], []), [])
assert_equal(products2.two_number_products([], [1]), [])

# Exercise 1 - 100 Sum
print("Exercise 1 - 100 Sum")
assert_equal(exercise1.one_hundred_sum([1, 98, 3, 97, 2, 99]), True)
# Can only be true if there are an even amount of numbers:
assert_equal(exercise1.one_hundred_sum([1, 98, 3, 100, 97, 2, 99]), False)
assert_equal(exercise1.one_hundred_sum([1, 98, 3, 97, 2, 95]), False)
assert_equal(exercise1.one_hundred_sum([]), False)
assert_equal(exercise1.one_hundred_sum([1]), False)

# Exercise 2 - Merge
print("Exercise 2 - Merge")
assert_equal(exercise2.merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
assert_equal(exercise2.merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
assert_equal(exercise2.merge([2, 3, 6], [1, 4, 5]), [1, 2, 3, 4, 5, 6])

# Exercise 3 - Needle in haystack
print("Exercise 3 - Needle in haystack")
assert_equal(exercise3.find_needle("abc", "abcdefg"), True)
assert_equal(exercise3.find_needle("c", "abcdefg"), True)
assert_equal(exercise3.find_needle("def", "abcdefg"), True)
assert_equal(exercise3.find_needle("fg", "abcdefg"), True)
assert_equal(exercise3.find_needle("g", "abcdefg"), True)
assert_equal(exercise3.find_needle("gh", "abcdefg"), False)
assert_equal(exercise3.find_needle("aa", "abcdefg"), False)
assert_equal(exercise3.find_needle("ccd", "abccdefg"), True)

# Exercise 4 - Largest product of 3
print("Exercise 4 - Largest product of 3")
assert_equal(exercise4.largest_product([]), None)
assert_equal(exercise4.largest_product([1]), None)
assert_equal(exercise4.largest_product([1, 2]), None)
assert_equal(exercise4.largest_product([1, 2, 3]), 6)
assert_equal(exercise4.largest_product([3, 2, 5, 1, 4]), 60)

# Exercise 5 - Resume picker
print("Exercise 5 - Resume picker")
assert_equal(exercise5.pick_resume([1, 2, 3, 4, 5, 6]), 3)
assert_equal(exercise5.pick_resume([1, 2, 3, 4, 5, 6, 7]), 3)
assert_equal(exercise5.pick_resume([1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)
assert_equal(exercise5.pick_resume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 4)
assert_equal(exercise5.pick_resume([]), None)
assert_equal(exercise5.pick_resume([1]), 1)
