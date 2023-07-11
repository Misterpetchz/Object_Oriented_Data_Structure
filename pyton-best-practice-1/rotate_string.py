print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split()

rounds = 0
loop_str1 = str1[-2:] + str1[:-2]
loop_str2 = str2[3:] + str2[0:3]
rounds += 1
print(rounds, loop_str1, loop_str2)

limit = False
while True:

    # right rotate
    loop_str1 = loop_str1[-2:] + loop_str1[:-2]
    # left rotate
    loop_str2 = loop_str2[3:] + loop_str2[0:3]

    rounds += 1
    if (rounds <= 5):
        print(rounds, loop_str1, loop_str2)

    if rounds == 5:
        print(" . . . . . ")
        limit = True

    elif (str1 == loop_str1 and str2 == loop_str2):
        if (limit == False):
            break
        print(rounds, loop_str1, loop_str2)
        break

print(f"Total of  {rounds} rounds.")
    