import stack
import queue
import linter
import print_manager
import solution


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Basic Stack operations
print("Basic Stack operations")
stack = stack.Stack()
stack.push('a')
assert_equal(stack.data[0], 'a')  # Push
stack.push('b')
assert_equal(stack.read(), 'b')   # Read
assert_equal(stack.pop(), 'b')    # Pop
assert_equal(stack.read(), 'a')
stack.pop()
assert_equal(stack.read(), None)
assert_equal(stack.pop(), None)

# JavaScript Linter
print("JavaScript linter")
linter = linter.Linter()
error_1 = "(var x = 2;"  # Syntax Error 1
error_2 = "var x = 2;)"  # Syntax Error 2
error_3 = "(var x = [1, 2, 3)];"  # Syntax Error 3
correct = "(var x = [1, 2, 3])"  # Correct
assert_equal(linter.lint(error_1), "( does not have closing brace")
assert_equal(linter.lint(error_2), ") does not have opening brace")
assert_equal(linter.lint(error_3), ") has mismatched opening brace")
assert_equal(linter.lint(correct), True)

# Basic Queue operations
print("Basic Queue operations")
queue = queue.Queue()
queue.enqueue('a')               # Enqueue
queue.enqueue('b')
queue.enqueue('c')
assert_equal(queue.read(), 'a')  # Read
assert_equal(queue.dequeue(), 'a')  # Dequeue
assert_equal(queue.read(), 'b')
queue.dequeue()
queue.dequeue()
assert_equal(queue.read(), None)
assert_equal(queue.dequeue(), None)

# Print manager
print("Print manager")
print_manager = print_manager.PrintManager()
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")
print_manager.run()

# Solution - reverse a string
print("Solution - reverse a string")
assert_equal(solution.reverse("abcde"), "edcba")
assert_equal(solution.reverse("a"), "a")
assert_equal(solution.reverse(""), "")
