from time import sleep
import sys
import requests

class Finder:
    __slots__ = ("protocol", "colors", "valids", "commands", "target")

    def __init__(self) -> None:
        self.colors = {'purplenegr': '\033[1;35m',
                'yellow': '\033[0;33m',
                'red': '\033[0;31m',
                'rednegr': '\033[1;31m',
                'green': '\033[0;32m',
                'endcolor': '\033[m'}
        self.commands = ["-w", "-p"]
        self.protocol = ""
        self.valids = [] #list: [str]

    def help_(self) -> None:
        print(f"""
        Command lines Finder:
            -h help to use
            -w Website target
            -p Protocol
            
            Example: python3 Sunev.py finder -w www.google.com -p https
                """)
                
    def main(self, list_args) -> None:
        dict_args = {"Site": list_args[0], "Protocol": list_args[1]}
        while 1:
            if not 'http' in dict_args["Protocol"] or not 'https' in dict_args["Protocol"]:
                print(f"{self.colors['rednegr']}Without http or https{self.colors['endcolor']}")
                break

            address = (dict_args["Protocol"] + ":" + "//" + dict_args["Site"] + '/').strip('\n')
            try:
                wordlist = open(f'Panel/pages.txt', 'r+')

                for test in wordlist.readlines():
                    link = (f'{address}{test}').strip('\n')
                    get = requests.get(link)
            
                    if get.status_code == 200:
                        print(f"\n{link} {self.colors['green']}is accessible and potentially an admin panel{self.colors['endcolor']}")
                        self.valids.append(link)
                    else:
                        sys.stdout.write(f"\r{link} {self.colors['red']}404{self.colors['endcolor']}")
            except KeyboardInterrupt:
                print(f"{self.colors['rednegr']}Program interrupt!{self.colors['endcolor']}")
            except:
                print(f"{self.colors['rednegr']}Digit a path/archive valid!{self.colors['endcolor']}")
            break

        for i in self.valids:
            print(f"{self.colors['green']}{i}{self.colors['endcolor']}")
