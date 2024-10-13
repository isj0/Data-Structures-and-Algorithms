import books_authors1
import books_authors2
import two_sum1
import two_sum2
import coin_game1
import coin_game2
import sum_swap
import array_max
import largest_subsection
import stocks
import anagrams1
import anagrams2
import group_sort
import solution1
import solution2
import solution3
import solution4
import solution5
import solution6


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Books with authors #1
print("Books with authors #1")

authors = [
  {"author_id": 1, "name": "Virginia Woolf"},
  {"author_id": 2, "name": "Leo Tolstoy"},
  {"author_id": 3, "name": "Dr. Seuss"},
  {"author_id": 4, "name": "J. K. Rowling"},
  {"author_id": 5, "name": "Mark Twain"}
]

books = [
  {"author_id": 3, "title": "Hop on Pop"},
  {"author_id": 1, "title": "Mrs. Dalloway"},
  {"author_id": 4, "title": "Harry Potter and the Sorcerer's Stone"},
  {"author_id": 1, "title": "To the Lighthouse"},
  {"author_id": 2, "title": "Anna Karenina"},
  {"author_id": 5, "title": "The Adventures of Tom Sawyer"},
  {"author_id": 3, "title": "The Cat in the Hat"},
  {"author_id": 2, "title": "War and Peace"},
  {"author_id": 3, "title": "Green Eggs and Ham"},
  {"author_id": 5, "title": "The Adventures of Huckleberry Finn"}
]

correct_result = [{'author': 'Dr. Seuss', 'title': 'Hop on Pop'}, {'author': 'Virginia Woolf', 'title': 'Mrs. Dalloway'}, {'author': 'J. K. Rowling', 'title': "Harry Potter and the Sorcerer's Stone"}, {'author': 'Virginia Woolf', 'title': 'To the Lighthouse'}, {'author': 'Leo Tolstoy', 'title': 'Anna Karenina'}, {'author': 'Mark Twain', 'title': 'The Adventures of Tom Sawyer'}, {'author': 'Dr. Seuss', 'title': 'The Cat in the Hat'}, {'author': 'Leo Tolstoy', 'title': 'War and Peace'}, {'author': 'Dr. Seuss', 'title': 'Green Eggs and Ham'}, {'author': 'Mark Twain', 'title': 'The Adventures of Huckleberry Finn'}]

assert_equal(books_authors1.connect_books_with_authors(books, authors), correct_result)

# Books with authors #2
print("Books with authors #2")
assert_equal(books_authors2.connect_books_with_authors(books, authors), correct_result)

# Two Sum 1
print("Two Sum 1")
assert_equal(two_sum1.two_sum([2, 0, 4, 1, 7, 9]), True)
assert_equal(two_sum1.two_sum([2, 0, 4, 5, 3, 9]), False)
assert_equal(two_sum1.two_sum([5, 5]), True)
assert_equal(two_sum1.two_sum([5]), False)

# Two Sum 2
print("Two Sum 2")
assert_equal(two_sum2.two_sum([2, 0, 4, 1, 7, 9]), True)
assert_equal(two_sum2.two_sum([2, 0, 4, 5, 3, 9]), False)
assert_equal(two_sum2.two_sum([5, 5]), True)
assert_equal(two_sum2.two_sum([5]), False)

# Coin game 1
print("Coin game 1")
assert_equal(coin_game1.game_winner(1), "them")
assert_equal(coin_game1.game_winner(2), "you")
assert_equal(coin_game1.game_winner(3), "you")
assert_equal(coin_game1.game_winner(4), "them")
assert_equal(coin_game1.game_winner(9), "you")
assert_equal(coin_game1.game_winner(10), "them")

# Coin game 2
print("Coin game 2")
assert_equal(coin_game2.game_winner(1), "them")
assert_equal(coin_game2.game_winner(2), "you")
assert_equal(coin_game2.game_winner(3), "you")
assert_equal(coin_game2.game_winner(4), "them")
assert_equal(coin_game2.game_winner(9), "you")
assert_equal(coin_game2.game_winner(10), "them")

# Sum swap
print("Sum swap")
assert_equal(sum_swap.sum_swap([5, 3, 2, 9, 1], [1, 12, 5]), [2, 0])
assert_equal(sum_swap.sum_swap([5, 3, 3, 7], [4, 1, 1, 6]), [3, 0])
assert_equal(sum_swap.sum_swap([5, 3, 3, 6], [4, 1, 1, 6]), None)
assert_equal(sum_swap.sum_swap([1, 2, 3, 4, 5], [6, 7, 8]), [2, 0])
assert_equal(sum_swap.sum_swap([10, 15, 20], [5, 30]), [0, 0])
assert_equal(sum_swap.sum_swap([5, 3, 1, 9, 0], [2, 12, 5]), None)
assert_equal(sum_swap.sum_swap([10], [5]), None)
assert_equal(sum_swap.sum_swap([], []), None)
assert_equal(sum_swap.sum_swap([], [5]), None)
assert_equal(sum_swap.sum_swap([10], []), None)

# Array max
print("Array max")
assert_equal(array_max.max([5, 8, 2, 0, 1]), 8)
assert_equal(array_max.max([]), None)
assert_equal(array_max.max([1]), 1)

# Largest subsection sum
print("Largest subsection sum")
assert_equal(largest_subsection.max_sum([3, -4, 4, -3, 5, -9]), 6)
assert_equal(largest_subsection.max_sum([1, 1, 0, -3, 5]), 5)
assert_equal(largest_subsection.max_sum([5, -2, 3, -8, 4]), 6)
assert_equal(largest_subsection.max_sum([2, -3, 1, 2, -1]), 3)
assert_equal(largest_subsection.max_sum([5, -8, 2, 1, 0]), 5)

# Stock predictions
print("Stock predictions")
assert_equal(stocks.is_increasing_triplet([22, 25, 21, 18, 19.6, 17, 16, 20.5]), True)
assert_equal(stocks.is_increasing_triplet([5, 2, 8, 4, 3, 7]), True)
assert_equal(stocks.is_increasing_triplet([8, 9, 7, 10]), True)
assert_equal(stocks.is_increasing_triplet([50, 51.25, 48.4, 49, 47.2, 48, 46.9]), False)

# Anagrams 1
print("Anagrams 1")
assert_equal(anagrams1.are_anagrams("a", "a"), True)
assert_equal(anagrams1.are_anagrams("enraged", "angered"), True)
assert_equal(anagrams1.are_anagrams("night", "thing"), True)
assert_equal(anagrams1.are_anagrams("nigh", "thing"), False)
assert_equal(anagrams1.are_anagrams("think", "thing"), False)

# Anagrams 2
print("Anagrams 2")
assert_equal(anagrams2.are_anagrams("a", "a"), True)
assert_equal(anagrams2.are_anagrams("enraged", "angered"), True)
assert_equal(anagrams2.are_anagrams("night", "thing"), True)
assert_equal(anagrams2.are_anagrams("nigh", "thing"), False)
assert_equal(anagrams2.are_anagrams("think", "thing"), False)

# Group sorting
print("Group sorting")
print(group_sort.group_sort(["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]))

# Solution 1
print("Solution 1")
basketball_players = [
     {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
     {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
     {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
     {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
     {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
   ]

football_players = [
     {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
     {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
     {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
     {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
     {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
   ]

assert_equal(solution1.find_multisport_athletes(basketball_players, football_players), ["Jill Huang", "Wanda Vakulskas"])

# Solution 2
print("Solution 2")
assert_equal(solution2.find_missing_number([2, 3, 0, 6, 1, 5]), 4)
assert_equal(solution2.find_missing_number([8, 2, 3, 9, 4, 7, 5, 0, 6]), 1)

# Solution 3
print("Solution 3")
assert_equal(solution3.find_greatest_profit([10, 7, 5, 8, 11, 2, 6]), 6)

# Solution 4
print("Solution 4")
assert_equal(solution4.greatest_product([5, -10, -6, 9, 4]), 60)

# Solution 5
print("Solution 5")
assert_equal(solution5.sort_temperatures([98, 99, 95, 105, 104, 98, 101, 99, 100, 97]), [95, 97, 98, 98, 99, 99, 100, 101, 104, 105])

# Solution 6
print("Solution 6")
assert_equal(solution6.longest_sequence_length([10, 5, 12, 3, 55, 30, 4, 11, 2]), 4)
assert_equal(solution6.longest_sequence_length( [19, 13, 15, 12, 18, 14, 17, 11]), 5)
