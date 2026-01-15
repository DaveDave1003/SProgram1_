from zasobnik import *

def math_validation(raw_data):

    parentheses_stack = Stack()

    for char in raw_data:
        if char == "(":
            parentheses_stack.push(char)

        elif char == ")":
            last_item = parentheses_stack.peek()

            if last_item == "(":
                parentheses_stack.pop()

            else: 
                return False
            
    if parentheses_stack.peek() is None:
        return True
    
    else:
        return False


text = ["((a+b)*c)", "(a+b)", "(a+b", "a+b)", ")(", ""]

for item in text:
    result = math_validation(item)
    print(f"{item} -> {result}")