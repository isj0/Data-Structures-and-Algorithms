import stack as stack_module


def reverse(string):
    stack = stack_module.Stack()
    new_string = ""

    for char in string:
        stack.push(char)

    while stack.read():
        new_string += stack.pop()

    return new_string
