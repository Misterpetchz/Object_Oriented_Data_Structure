print("*** Rabbit & Turtle ***")
d, vr, vt, vf = input('Enter Input : ').split()
dt = int(d) / (int(vt) - int(vr))
distance = int(vf) * dt
print(f"{distance:.2f}")