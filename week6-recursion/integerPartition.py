def partition(n, m, path):
    if n == 0:
        if m == 0:
            return [0]
        return [(' + '.join(map(str, path)))]
    if n < 0 or m == 0:
        return []
    return partition(n - m, m, path + [m]) + partition(n, m - 1, path)

def show_line(lst, round, idx=0):
    output = []
    if round == 0:
        output.append('. . .')
        return output
    else:
        if idx < round:
            output.append(lst[idx])
            result = show_line(lst, round, idx + 1)
            output.extend(result)
            return output
        else:
            output.append('. . .')
            return output
        
def display(lst, idx=0):
    if idx < len(lst):
        print(lst[idx])
        return display(lst, idx + 1)

inp1, inp2 = map(int, input('Enter n, s: ').split())
portion = partition(inp1, inp1, [])
totals = len(portion)
if totals == inp2:
    display(portion)
else:
    display(show_line(portion, inp2))
print(f'Total: {totals}')