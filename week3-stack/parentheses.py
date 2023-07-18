class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __repr__(self) -> str:
        return f'{self.items}'
    
def check_parentheses(input_str):
    s = Stack()

    matching = {'(': ')', '[': ']', '{': '}'}

    for char in input_str:
        if char in '{[(':
            s.push(char)
        else:
            if char in '}])':
                if s.size() > 0:
                    if s.pop() != matching[s.pop()]:
                        return False
                else:
                    return False
    return len(s.items) == 0

input_str = input("Enter Input : ")

if check_parentheses(input_str):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")