from DoS.configs_dos import DenialOfService
from Panel.configs_panel import Finder
from Proxy.configs_proxy import Proxy
from sys import argv
from time import sleep
import os

class Commands:
    __slots__ = ("objects_class", "verify_digit", "undefinied", "mode", "parameters", "colors")
    
    def __init__(self, mode: str) -> None:
        self.parameters = {}
        self.mode = mode
        self.objects_class = {"denial": [DenialOfService(), DenialOfService().commands],
                        "finder": [Finder(), Finder().commands], "proxy": [Proxy(), Proxy().commands],
                        "comp": ["-h", "-r"]} ##Comandos de cada metodo
        self.verify_digit = {mode: [i for i in argv if mode != "comp" and i in self.objects_class[mode][1]]} #Comandos digitados pelo usuário
        self.undefinied = list(set([i for i in self.objects_class[mode] if mode != "comp" for i in self.objects_class[mode][1] if i not in self.verify_digit[mode]])) #Comandos que faltam atribuir
        self.colors = {'purplenegr': '\033[1;35m', 'yellow': '\033[0;33m', 'red': '\033[0;31m',
                    'rednegr': '\033[1;31m', 'green': '\033[0;32m', 'endcolor': '\033[m'}

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

    def filter_arguments(self) -> None:
        if self.mode in ["comp"] and argv[2] == "-h":
            print(f"""
            Command lines
                Digit [mode] -h for help menu               
                Example: python3 Sunev.py -h denial
                Install dependencies: python3 Sunev.py -d
                Options menu: denial | finder | proxy
            """)
        elif self.mode in self.objects_class and argv[2] == "-h":
            self.objects_class[self.mode][0].help_()
        elif self.undefinied:
            print(f"{self.colors['rednegr']}Error undefined parameters:{self.colors['endcolor']} {(' ').join(self.undefinied)}")
        elif self.mode in self.objects_class and argv[2] == "-r":
            self.requirements()
        elif self.verify_digit[self.mode] == self.objects_class[self.mode][1]:
            for i in range(len(self.verify_digit[self.mode])):
                def_parameters = self.verify_digit[self.mode][i]
                self.parameters[def_parameters] = argv[int(argv.index(def_parameters)+1)]

            list_param = list(self.parameters.values())
            self.objects_class[self.mode][0].main(list_param) #Instancia da classe atual com o metodo main.
