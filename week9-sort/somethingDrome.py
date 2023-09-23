def metadrome(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True

def plaindrome(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def katadrome(lst):
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False
    return True

def nialpdrome(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            return False
    return True

def check_drome(lst):
    if len(set(lst)) == 1:
        return "Repdrome"
    elif metadrome(lst):
        return "Metadrome"
    elif plaindrome(lst):
        return "Plaindrome"
    elif katadrome(lst):
        return "Katadrome"
    elif nialpdrome(lst):
        return "Nialpdrome"
    else:
        return "Nondrome"
    
print(check_drome(input('Enter Input : ')))