def countdown(lst):
    countdownList = []
    stack = []
    for num in lst:
        if len(stack) == 0:
            stack.append(num)
            if num == 1:
                countdownList.append(stack)
                stack = []
        elif num == 1:
            stack.append(num)
            countdownList.append(stack)
            stack = []
        elif stack[-1] == num+1:
            stack.append(num)
        else:
            stack = [num]
    return [len(countdownList), countdownList]

print("*** Fun with countdown ***")
lst = [int(x) for x in input('Enter List : ').split()]
print(countdown(lst))
