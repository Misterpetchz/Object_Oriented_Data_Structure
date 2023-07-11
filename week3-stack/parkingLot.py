class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        res = self.items[-1]
        self.items = self.items[:-1]
        return res
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)
    
    def __repr__(self) -> str:
        return f'{self.items}'
    
def parkingLot(max, parking_cars, state, target):

    # add Stack
    max = int(max)
    if parking_cars == '0':
        cars = Stack()
    else:
        parking_cars = [int(car) for car in parking_cars.split(',')]
        cars = Stack()
        for car in parking_cars:
            cars.items.append(car)
    
    # Action State
    target = int(target)
    if state == 'arrive':
        if target in cars.items:
            print(f'car {target} already in soi')
            print(cars.items)
        elif len(cars.items) == max:
            print(f'car {target} cannot arrive : Soi Full')
            print(cars.items)
        else:
            cars.items.append(target)
            print(f'car {target} arrive! : Add Car {target}')
            print(cars.items)
    elif state == 'depart':
        if target not in cars.items and len(cars.items) == 0:
            print(f'car {target} cannot depart : Soi Empty')
            print(cars.items)
        elif target not in cars.items:
            print(f'car {target} cannot depart : Dont Have Car {target}')
            print(cars.items)
        else:
            temps_cars = Stack()
            for car in range(len(cars.items)-1, -1, -1):
                if cars.items[car] != target:
                    temps_cars.push(cars.pop())
                else:
                    cars.pop()
                    break
            for car in range(len(temps_cars.items)-1, -1, -1):
                cars.push(temps_cars.items[car])

            print(f'car {target} depart ! : Car {target} was remove')
            print(cars.items)

print("******** Parking Lot ********")
input_detail = input("Enter max of car,car in soi,operation : ").split()
parkingLot(*input_detail)