import requests

class Finder:
    __slots__ = ("protocol", "colors", "valids")

    def __init__(self) -> None:
        self.colors = {'purplenegr': '\033[1;35m',
                'yellow': '\033[0;33m',
                'red': '\033[0;31m',
                'rednegr': '\033[1;31m',
                'green': '\033[0;32m',
                'endcolor': '\033[m'}
        self.protocol = ""
        self.valids = [] #list: [str]

    def main(self, site, protocol) -> None:
        while 1:
            if not 'http' in protocol or not 'https' in protocol:
                print(f"{self.colors['rednegr']}Without http or https{self.colors['endcolor']}")
                break

            address = (protocol + ":" + "//" + site + '/').strip('\n')
            try:
                wordlist = open(f'Panel/pages.txt', 'r+')

                for test in wordlist.readlines():
                    link = (f'{address}{test}').strip('\n')
                    get = requests.get(link)
            
                    if get.status_code == 200:
                        print(f"{link} {self.colors['green']}is accessible and potentially an admin panel{self.colors['endcolor']}")
                        self.valids.append(link)
                    else:
                        print(f"{link} {self.colors['red']}error 404{self.colors['endcolor']}")
            except KeyboardInterrupt:
                print(f"{self.colors['rednegr']}Program interrupt!{self.colors['endcolor']}")
            except:
                print(f"{self.colors['rednegr']}Digit a path/archive valid!{self.colors['endcolor']}")
            break

        for i in self.valids:
            print(f"{self.colors['green']}{i}{self.colors['endcolor']}")