class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
def manageStack(str):
    s = Stack()

    for cmd in str:
        cmd = cmd.split()
        if cmd[0] == 'A':
            s.push(int(cmd[1]))
            print(f'Add = {cmd[1]}')
        elif cmd[0] == 'P':
            if not s.isEmpty():
                print(f'Pop = {s.pop()}')
            else:
                print('-1')
        elif cmd[0] == 'D':
            temp = Stack()
            delete = Stack()
            while not s.isEmpty():
                number = s.pop()
                if number != int(cmd[1]):
                    temp.push(number)
                else:
                    delete.push(number)

            if delete.isEmpty():
                print('-1')
            else:
                while not delete.isEmpty():
                    print(f'Delete = {delete.pop()}')

            while not temp.isEmpty():
                s.push(temp.pop())

        elif cmd[0] == 'LD':
            temp = Stack()
            ld = Stack()
            while not s.isEmpty():
                number = s.pop()
                if number >= int(cmd[1]):
                    temp.push(number)
                else:
                    ld.push(number)
            
            if ld.isEmpty():
                print('-1')
            else:
                for i in ld.items:
                    print(f'Delete = {i} Because {i} is less than {int(cmd[1])}')
            while not temp.isEmpty():
                s.push(temp.pop())

        elif cmd[0] == 'MD':
            temp = Stack()
            ld = Stack()
            while not s.isEmpty():
                number = s.pop()
                if number <= int(cmd[1]):
                    temp.push(number)
                else:
                    ld.push(number)
            
            if ld.isEmpty():
                print('-1')
            else:
                for i in ld.items:
                    print(f'Delete = {i} Because {i} is less than {int(cmd[1])}')
            while not temp.isEmpty():
                s.push(temp.pop())
    print(f'Value in Stack = {s.items}')

input_str = input('Enter Input : ').split(',')
manageStack(input_str)