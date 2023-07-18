class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __repr__(self) -> str:
        return f'{self.items}'
    
def colorCrush(colors):
    stack = Stack()
    combo = 0

    # check colors
    
    for color in colors:
        if stack.isEmpty():
            stack.push(color)
        elif stack.items[-1] == color:
            stack.push(color)
            if stack.size() >= 3:
                if stack.items[-1] == stack.items[-2] == stack.items[-3]:
                    combo += 1
                    for _ in range(3):
                        stack.pop()
        else:
            stack.push(color)
    
    # create stack to contain remain colors
    remaining_stack = Stack()

    while not stack.isEmpty():
        color = stack.pop()
        remaining_stack.push(color)

    if remaining_stack.size() != 0:
        print(remaining_stack.size())
        print(''.join(remaining_stack.items))
        if combo > 1:
            print(f'Combo : {combo} ! ! !')
    else:
        print(remaining_stack.size())
        print('Empty')
        if combo > 1:
            print(f'Combo : {combo} ! ! !')

colors = input("Enter Input : ").split()
colorCrush(colors)
