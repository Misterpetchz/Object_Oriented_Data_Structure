print(" *** Wind classification ***")
v = float(input('Enter wind speed (km/h) : '))
if (v < 0):
    print("!!!Wrong value can't classify.")
elif (0 <= v < 52):
    print('Wind classification is Breeze.')
elif (52 <= v < 56):
    print('Wind classification is Depression.')
elif (56 <= v < 102):
    print('Wind classification is Tropical Storm.')
elif (102 <= v < 209):
    print('Wind classification is Typhoon.')
elif (v >= 209):
    print('Wind classification is Super Typhoon.')