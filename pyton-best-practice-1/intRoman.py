class MyInt:
    def __init__(self, num):
        self.num = num

    def toRoman(self):
        roman_num = ""
        num_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        num_temp = self.num
        for value, symbol in num_map.items():
            while num_temp >= value:
                roman_num += symbol
                num_temp -= value

        return roman_num
    

    def __add__(self, other):
        result = int((self.num + other.num) * 1.5)
        return MyInt(result)


print(' *** class MyInt ***')
num1, num2 = map(int,input('Enter 2 number : ').split())
a = MyInt(num1)
b = MyInt(num2)
print(a.toRoman())
print(b.toRoman())
print(f"{num1} + {num2} = {(a+b).num}")
