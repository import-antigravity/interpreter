from datetime import datetime
from sys import argv


class Program:
    def __init__(self, code: str):
        self.code = code
        self.acc = 0

    @staticmethod
    def h():
        print("Hello, world!")

    def q(self):
        print(self.code)

    @staticmethod
    def __beer(i: int) -> str:
        if i > 0:
            plural = "s" if i > 1 else ""
            return ' '.join([str(i), "bottle" + plural, "of", "beer"])
        elif i == 0:
            return "No more bottles of beer"

    @staticmethod
    def __print_stanza(i: int):
        print(' '.join([Program.__beer(i), "on", "the", "wall,", Program.__beer(i) + ","]))
        print(' '.join(["Take one down and pass it around," if i > 0 else "Go to the store and buy some more,",
                        Program.__beer(i - 1 if i > 0 else 99), "on", "the", "wall!"]))
        print()

    @staticmethod
    def nine():
        i = 99
        while i >= 0:
            Program.__print_stanza(i)
            i -= 1

    def plus(self):
        self.acc += 1
        print()

    def execute(self):
        available_commands = {
            "h": self.h,
            "q": self.q,
            "9": self.nine,
            "+": self.plus
        }
        commands = self.code.split()
        for command in commands:
            try:
                available_commands.get(command.lower())()
            except TypeError:
                pass


try:
    if argv[1].split('.')[-1] == "hq":
        with open(argv[1]) as fp:
            Program(fp.read()).execute()
    else:
        print("Unknown file " + "\"" + argv[1] + "\"")
except IndexError:
    try:
        print("HQ9+ Interpreter 1.0.0 " + datetime.now().strftime("%Y-%m-%d %H:%M"))
        print("Type \"quit\" to exit")
        while True:
            s = input("+ ")
            if s == "quit":
                break
            p = Program(s)
            p.execute()
    except KeyboardInterrupt:
        print()
