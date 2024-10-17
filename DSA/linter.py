# Stack implementation in action

import stack

class Linter:

    def __init__(self):
        self.stack = stack.Stack()

    def lint(self, text):
        while self.stack.read():
            self.stack.pop()

        matching_braces = {"(" : ")", "[" : "]", "{" : "}"}

        for char in text:

            if char in matching_braces.keys():
                self.stack.push(char)

            elif char in matching_braces.values():
                if not self.stack.read():
                    return char + " does not have a matching brace"
                else:
                    popped_opening_brace = self.stack.pop()

                    if char != matching_braces.get(popped_opening_brace):
                        return char + " has mismatched opening brace"
        
        if self.stack.read():
            return self.stack.read() + " does not have closing brace"
        
        return True
    

linter = Linter()
print(linter.lint("(var x = 2;"))