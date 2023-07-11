print('*** Fun with permute ***')
val = input('input : ').split(',')

numbers = list(map(int, val))

print("Original Cofllection: ", numbers)

source = [[]]

for i in numbers:
    new_source = []

    for j in source:

        for k in range(len(j) + 1):
            new_source.append(j[:k] + [i] + j[k:])
            source = new_source

print("Collection of distinct numbers:\n", source)


