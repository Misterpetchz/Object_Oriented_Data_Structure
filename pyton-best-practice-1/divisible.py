print(' *** Divisible number ***')
number = int(input('Enter a positive number : '))
if (number <= 0):
    print(f"{number} is OUT of range !!!")
else:
    list = []
    for i in range(1, number + 1):
        if (number % i == 0):
            list.append(i)
    str = ' '.join(map(str, list))

count = len(list)
print("Output ==>", str)
print('Total ==>', count)
    