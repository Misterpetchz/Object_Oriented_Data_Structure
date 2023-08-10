def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n
    
inp = input('Enter Number : ')
print(f'{inp}! = {factorial(int(inp))}')