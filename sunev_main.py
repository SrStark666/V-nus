from src import Commands
from sys import argv

class Start:
    __slots__ = ("colors")

    def __init__(self) -> None:
        self.colors = {'purplenegr': '\033[1;35m',
                'yellow': '\033[0;33m',
                'red': '\033[0;31m',
                'rednegr': '\033[1;31m',
                'green': '\033[0;32m',
                'endcolor': '\033[m'}

    def main(self) -> None:
        try:
            obj_class = Commands(argv[1])
            obj_class.filter_arguments()
        except IndexError:
            print(f"{self.colors['red']}No parameter was set\nDigit python3 sunev_main.py comp -h for help{self.colors['endcolor']}")
        except KeyboardInterrupt:
            print(f"{self.colors['red']}Program interrupt{self.colors['endcolor']}")
        except KeyError:
            print(f"{self.colors['rednegr']}Key ({argv[1]}) not found{self.colors['endcolor']}")

obj_class = Start()
obj_class.main()