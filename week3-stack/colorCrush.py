# Didn't create Stack Class

def colorCrush(colors):
    stack = []
    combo = 0

    for color in colors:
        if not stack:
            stack.append(color)
        elif stack[-1] == color:
            stack.append(color)
            if len(stack) >= 3:
                if stack[-1] == stack[-2] == stack[-3]:
                    combo += 1
                    stack = stack[:-3]
        else:
            stack.append(color)
        
    remaining_color = stack[::-1]
    length = len(remaining_color)
    if length != 0:
        print(length)
        print(''.join(remaining_color))
        if combo > 1:
            print(f'Combo : {combo} ! ! !')
    else:
        print(length)
        print('Empty')
        if combo > 1:
            print(f'Combo : {combo} ! ! !')

input_str = input("Enter Input : ").split()
colorCrush(input_str)