class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []
        return "game restarted"

    def play(self, word):
        if word.lower() in self.words:
            # return "game over"
            pass
        if self.words:
            last_word = self.words[-1].lower()
            if last_word[-2:] != word[:2].lower():
                return f"'{word}' -> game over"

        self.words.append(word)
        return f"'{word}' -> {self.words}"

torkham = TorKham()

print("*** TorKham HanSaa ***")

command = input("Enter Input : ")

command_list = command.split(',')

for cmd in command_list:
    if cmd[0] == 'P':
        word = cmd[2:]
        result = torkham.play(word)
        print(result)

    elif cmd[0] == 'R':
        result = torkham.restart()
        print(result)

    elif cmd[0] == 'X':
        break

    else:
        print(f"'{cmd}' is Invalid Input !!!")
        break