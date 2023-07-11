# Didn't create Stack Class

def manageStack(input_str):
    stack = []

    for cmd in input_str:
        cmd = cmd.split()
        if cmd[0] == 'A':
            stack.append(int(cmd[1]))
            print(f"Add = {cmd[1]}")
        elif cmd[0] == 'P':
            if len(stack) != 0:
                last_stack = stack.pop()
                print(f'Pop = {last_stack}')
            else:
                print('-1')
        elif cmd[0] == 'D':
            if len(stack) != 0:
                deleted_numbers = [number for number in stack if number != int(cmd[1])]
                removed_count = len(stack) - len(deleted_numbers)
                stack = deleted_numbers
                for _ in range(removed_count):
                    print(f'Delete = {cmd[1]}')
            else:
                print('-1')
        elif cmd[0] == 'LD':
            if len(stack) != 0:
                deleted_numbers = []
                for _ in range(len(stack)-1, -1, -1):
                    if stack[_] < int(cmd[1]):
                        deleted_numbers.append(stack.pop(_))
                
                if deleted_numbers:
                    for deleted_num in deleted_numbers:
                        print(f'Delete = {deleted_num} Because {deleted_num} is less than {cmd[1]}')
            else:
                print('-1')
        elif cmd[0] == 'MD':            
            if len(stack) != 0:
                deleted_numbers = []
                for _ in range(len(stack)-1, -1, -1):
                    if stack[_] > int(cmd[1]):
                        deleted_numbers.append(stack.pop(_))
                
                if deleted_numbers:
                    for deleted_num in deleted_numbers:
                        print(f'Delete = {deleted_num} Because {deleted_num} is more than {cmd[1]}')
            else:
                print('-1')

    print(f'Value in Stack = {stack}')


input_str = input("Enter Input : ").split(',')
manageStack(input_str)
