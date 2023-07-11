# Didn't create Stack Class

class Calculator:
    def __init__(self):
        self.stack = []
        self.invalid = False

    def run(self, instructions):

        for instruction in instructions:
            if instruction.isnumeric():
                self.stack.append(int(instruction))
            elif instruction == '+':
                if len(self.stack) >= 2:
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    self.stack.append(int(num1 + num2))
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == '-':
                if len(self.stack) >= 2:
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    self.stack.append(int(num1 - num2))
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == '*':
                if len(self.stack) >= 2:
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    self.stack.append(int(num1 * num2))
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == '/':
                if len(self.stack) >= 2:
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    if num2 != 0:
                        self.stack.append(int(num1 / num2))
                    else:
                        print("Invalid instruction:", instruction)
                        self.invalid = True
                        break
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == 'DUP':
                if len(self.stack) >= 1:
                    self.stack.append(self.stack[-1])
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == 'POP':
                if len(self.stack) >= 1:
                    self.stack.pop()
                else:
                    print("Invalid instruction:", instruction)
                    self.invalid = True
                    break
            elif instruction == 'PSH':
                num = int(instructions[instructions.index('PSH') + 1])
                self.stack.append(num)
            else:
                print("Invalid instruction:", instruction)
                self.invalid = True
                break

    def getValue(self):
        if len(self.stack) > 0 :
            return self.stack[-1]
        else:
            return 0
        

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = Calculator()
machine.run(arg)

if machine.invalid != True:
    print(machine.getValue())

# if case Invalid instruction not return but if empty stack will return 0