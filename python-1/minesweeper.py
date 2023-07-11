def num_grid(lst):

    rows = len(lst)
    cols = len(lst[0])
    
    result = [['0' if cell == '-' else cell for cell in row] for row in lst]

    for i in range(rows):
        for j in range(cols):

            if result[i][j] == '#': 
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < rows and 0 <= y < cols and result[x][y] != '#':
                        result[x][y] = str(int(result[x][y]) + 1)
    return result

print("*** Minesweeper ***")
lst_input = []
input_list = input('Enter input(5x5) : ').split(",")
for e in input_list:
    lst_input.append([i for i in e.split()])

print("\n", *lst_input, sep="\n")

print("\n", *num_grid(lst_input), sep="\n")