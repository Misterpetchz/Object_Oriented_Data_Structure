class Monkey:
    gen_id = 0
    def __init__(self, name, strength, intelligence, agility):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = Monkey.gen_id
        Monkey.gen_id += 1
        
    def __repr__(self) -> str:
        return str(self.id) + '-' + str(self.name)
    
    def getAttribute(self, attr):
        if attr == 'name':
            return self.name
        elif attr == 'str':
            return self.str
        elif attr == 'int':
            return self.int
        elif attr == 'agi':
            return self.agi
        
    def compare(self, attr_lst, other, order):
        if order == 'A':
            for attr in attr_lst:
                if self.getAttribute(attr) < other.getAttribute(attr):
                    return True
                elif self.getAttribute(attr) > other.getAttribute(attr):
                    return False
        else:
            for attr in attr_lst:
                if self.getAttribute(attr) > other.getAttribute(attr):
                    return True
                elif self.getAttribute(attr) < other.getAttribute(attr):
                    return False
        return True

def merge(arr1, arr2, attr_lst, order):
    res = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i].compare(attr_lst, arr2[j], order):
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

def mergeSort(arr, attr_lst, order):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid], attr_lst, order)
    right = mergeSort(arr[mid:], attr_lst, order)
    return merge(left, right, attr_lst, order)
    
inp = input('Enter Input: ').split('/')
order = inp[0]
if not inp[1]:
    attr_lst = []
else:
    attr_lst = inp[1].split(',')
monkeys = inp[2].split(',')
monkey_lst = []
for monkey in monkeys:
    attr = monkey.split()
    monkey_lst.append(Monkey(attr[0], int(attr[1]), int(attr[2]), int(attr[3])))

if attr_lst:
    monkey_lst = mergeSort(monkey_lst, attr_lst, order)
print(f"[{', '.join([f'{monkey}' for monkey in monkey_lst])}]")