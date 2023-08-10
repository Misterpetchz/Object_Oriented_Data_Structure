def length(txt):
    if txt == '':
        return 0
    else:
        return 1 + length(txt[1:])

def show(txt, idx=0, toggle=False):
    special_chars = ['*', '~']
    if idx < length(txt):
        print(txt[idx] + special_chars[toggle], end='')
        show(txt, idx + 1, not toggle)
    else:
        print()

inp1 = input('Enter Input : ')
show(inp1)
print(length(inp1))