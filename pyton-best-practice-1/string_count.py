print(" *** String count ***")
message = input("Enter message : ")
upper = 0
lower = 0
upper_set = set()
lower_set = set()

for char in message:
    if char.isupper():
        upper += 1
        upper_set.add(char)
    elif char.islower():
        lower += 1
        lower_set.add(char)

upper_str = '  '.join(sorted(upper_set))
lower_str = '  '.join(sorted(lower_set))

print("No. of Upper case characters :", upper)
print("Unique Upper case characters :", upper_str)
print("No. of Lower case Characters :", lower)
print("Unique Lower case characters :", lower_str)