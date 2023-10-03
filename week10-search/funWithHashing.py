class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = [None] * table_size

    def insert(self, key, value):
        total = 0
        if not self.isFull():
            for chr in key:
                total += ord(chr)
            idx = total % self.table_size

            if self.table[idx] is None:
                self.table[idx] = Data(key, value)

            elif self.table is not None:
                collision = 0
                print(f'collision number {collision + 1} at {idx}')

                while self.table[idx] is not None:
                    collision += 1
                    new_idx = (idx + collision * collision) % self.table_size
                    if self.table[new_idx] is None:
                        self.table[new_idx] = Data(key, value)
                        break
                    if self.max_collision <= collision:
                        print('Max of collisionChain')
                        break
                    print(f'collision number {collision + 1} at {new_idx}')

    def isFull(self):
        return None not in self.table
    
    def print_table(self):
        for i in range(len(self.table)):
            print(f'#{i+1}      {self.table[i]}')
        print("---------------------------")
        
print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')
table_size, max_collision = map(int, inp[0].split())
data_list = inp[1].split(',')

hash = Hash(table_size, max_collision)
for data in data_list:
    key, value = data.split()
    hash.insert(key, value)
    hash.print_table()
    if hash.isFull():
        print("This table is full !!!!!!")
        break