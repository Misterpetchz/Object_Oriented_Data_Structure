def is_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

inp = [int(x) for x in input('Enter Input : ').split()]
if is_sorted(inp):
    print('Yes')
else:
    print('No')