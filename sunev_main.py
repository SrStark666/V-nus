from DoS.configs_dos import DenialOfService
from Panel.configs_panel import Finder
from Proxy.configs_proxy import proxy_
from time import sleep
from sys import argv
import socket
import os

class Start:
    __slots__ = ("commands","undefinied", "arg_denial", "arg_finder", "colors", "arg_complement", "point", "modes_smallen", "arg_proxy", "proxy")

    def __init__(self) -> None:
        self.colors = {'purplenegr': '\033[1;35m',
                'yellow': '\033[0;33m',
                'red': '\033[0;31m',
                'rednegr': '\033[1;31m',
                'green': '\033[0;32m',
                'endcolor': '\033[m'}

        self.commands = {"denial": ["-t", "-p", "-th", "-pkg", "-b"],
                        "finder": ["-w", "-p"], 
                        "proxy": ["-a"],
                        "complement": ["-h"]}
                        
        self.arg_denial = [i for i in argv if i in self.commands["denial"]] #list: [str] -> [argv]
        self.arg_finder = [i for i in argv if i in self.commands["finder"]]
        self.arg_complement = [i for i in argv if i in self.commands["complement"]]
        self.arg_proxy = [i for i in argv if i in self.commands["proxy"]]
        self.undefinied = [] #list: [str] -> [argv not in self.commands]
        self.modes_smallen = ["finder", "proxy"] #Modes with arguments less than 5
        self.proxy = proxy_("1")

    def help_all(self, mode) -> None: ##Panel for help users 
        if "denial" in mode:
            print(f"""
        Command lines DoS:
            {self.commands["complement"][0]} help to use
            {self.commands["denial"][0]} for especifies of target
            {self.commands["denial"][1]} for especifies of port
            {self.commands["denial"][2]} number of threads
            {self.commands["denial"][3]} number of packages for send
            {self.commands["denial"][4]} for especifies of lenght bytes

            Example: python3 Sunev.py -denial -t 127.0.0.1 -p 80 -th 5 -pkg 3 -b 1048
                """)

        elif "finder" in mode:
            print(f"""
        Command lines Finder:
            {self.commands["complement"][0]} help to use
            {self.commands["finder"][0]} Website target
            {self.commands["finder"][1]} Protocol
            
            Example: python3 Sunev.py -finder -w www.google.com -p https
                """)

        elif "main" in mode:
            print(f"""
            Digit [mode] -h for help menu               
            Example: python3 Sunev.py -h denial
            Install dependencies: python3 Sunev.py -d
            Options menu: -denial | -finder | -proxy
            """)

        elif "proxy" in mode:
            print(f"""
        Command Lines Proxy:
            {self.commands['complement'][0]} help to use
            {self.commands['proxy'][0]} name archive for save list proxy.txt [Optional]

            Example: python3 sunev.py -proxy -a list_proxy.txt
            """)

    def requirements(self) -> str: ##Install requirements
        req = ["requests", "subprocess", "os",
                "socket", "threading", "sys", "re"]

        for i in req:
            os.system(f"pip install {i}")
            sleep(2)

        print(f"Instalação concluída com sucesso!!")
        sleep(2)
        print("\x1b[H\x1b[2J\x1b[3J", end="") #Limpar a tela
        for i in req:
            print(f"Pacotes instalados: {i}")

        return req

    def filter_arguments(self, mode: str, attr: str) -> None: #mode: str [-mode], attr: str[self.arg_denial]
        if f"-{mode}" in argv[1]:
            if len(argv) == 3 and "-h" in self.commands["complement"]:
                self.help_all(f"{mode}")
                exit()

            elif mode not in self.modes_smallen and len(attr) >= 1 and len(attr) < 5:
                for commands in self.commands[mode]:           
                    if not commands in attr:      
                        self.undefinied.append(commands)
                print(f"Error undefined parameters: {(' ').join(self.undefinied)}")

            elif attr == self.commands[mode]:
                if mode == "denial":
                    port = int(argv.index("-p")+1)
                    threads = int(argv.index("-th")+1)
                    packages = int(argv.index("-pkg")+1)
                    byt = int(argv.index("-b")+1)

                    params = {"Host": socket.gethostbyname(argv[3]),
                                "Port": int(argv[port]), 
                                "Threads": int(argv[threads]),
                                "Packages": int(argv[packages]),
                                "Bytes": int(argv[byt])}

                    obj_class = DenialOfService(params["Host"], params["Port"])
                    obj_class.multi(params["Threads"], params["Bytes"], params["Packages"])

                elif mode == "finder":
                    website = int(argv.index("-w")+1)
                    protocol = int(argv.index("-p")+1)
                    
                    params = {"Website": str(argv[website]),
                                "Protocol": str(argv[protocol])}
                                
                    obj_class = Finder()
                    obj_class.main(params["Website"],
                                    params["Protocol"])

                elif mode == "proxy":
                    params = {"Save": None}
                    try:
                        save = int(argv.index("-a"))
                        if argv[save+1] != "1":
                            params["Save"] = argv[save+1]
                    except ValueError:
                        params["Save"] = "1"
                    proxy_(params["Save"])

    def main(self) -> None:
        try:
            while 1:
                if "-h" in argv[1]:
                    self.help_all("main")
                    break

                elif "-proxy" in argv[1]:
                    self.point = self.arg_proxy
                    self.filter_arguments("proxy", self.point)
                    break

                elif len(argv) == 2 and argv[1] in ["-d"]:
                    self.requirements()
                    break

                elif "-denial" in argv[1]:
                    self.point = self.arg_denial
                    self.filter_arguments("denial", self.point)
                    break

                elif "-finder" in argv[1]:
                    self.point = self.arg_finder
                    self.filter_arguments("finder", self.point)
                    break

                elif not len(self.arg_denial) and not len(self.arg_finder) and not len(self.arg_proxy) and not len(self.arg_complement):
                    print("No parameter set, digit surnev.py -h for help.")
                    break
        except:
            print("Parameter error, verify arguments")

obj_class = Start()
obj_class.main()