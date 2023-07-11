# Didn't create Stack Class

def check_parentheses(input_str):
    stack = []
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in input_str:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack:
                return False
            last_opening = stack.pop()
            if matching[last_opening] != char:
                return False
        
    return len(stack) == 0

input_str = input("Enter Input : ")

if check_parentheses(input_str):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")