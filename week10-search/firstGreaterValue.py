def findGreater(arr, targets):
    arr.sort()

    for target in targets:
        found = False
        for num in arr:
            if num > target:
                print(num)
                found = True
                break
        
        if not found:
            print('No First Greater Value')

inp = input('Enter Input : ').split('/')
arr = list(map(int, inp[0].split()))
targets = list(map(int, inp[1].split()))
findGreater(arr, targets)