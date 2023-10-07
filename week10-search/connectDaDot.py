def distance(x, y):
    return sqRoot((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def shortest_point(l, point):
    return min(l, key=lambda p: distance(p, point))

def sqRoot(n):
    if n < 0:
        return -1
    return n ** 0.5

def draw(lst, point):
    if len(lst) == 0:
        return
    if point in lst:
        lst.remove(point)
    shortest = shortest_point(lst, point)
    print(f'{point} -> {shortest} | The distance is {distance(shortest, point):.4f}')
    lst.remove(shortest)
    draw(lst, shortest)

inp, start = input('Enter a list of points: ').split('/')
start = [float(x) for x in start.split()]

inp = inp.split(',')
inp = [x.split() for x in inp]
inp = [[float(y) for y in x] for x in inp]
lst = inp.copy()

if start in lst:
    draw(inp, start)
else:
    print(f'{start} is not in {inp}')