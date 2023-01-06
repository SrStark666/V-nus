import requests
import re

class Proxy:
    __slots__ = ("commands")
    
    def __init__(self) -> None:
        self.commands = ["-y", "-a"]
        
    def help_(self) -> None:
        print(f"""
            Command Lines Proxy:
                -h help to use
                -a name archive for save list proxy.txt
                -y for save archive

                Example: python3 sunev.py -proxy -y -a list_proxy.txt
            """)
        
    def main(self, list_args: list) -> list[dict[str: int]]: #list: [dict{http://127.0.0.1:80, https://127.0.0.1:80}]
        dict_args = {"Save": list_args[0], "Name-Archive": list_args[1]}
        save = dict_args["Save"]
        valid_proxys = []
        get = requests.get("https://free-proxy-list.net/")
        html = get.text
        html = html.split("UTC."); html = html[1].split("</")
        proxy_list = html[0].split("\n")

        if dict_args["Save"] != "-y" and not re.search(".txt", dict_args["Save"]):
            save = save + ".txt"

        for i in proxy_list:
            if i != "":
                proxy = i.replace("\n", "").split(":")[0]
                port = i.replace("\n", "").split(":")[1]

                dict_ = {"http": f"http://{proxy}:{port}",
                    "https": f"https://{proxy}:{port}"}

                valid_proxys.append(dict_)

        with open(f"Proxy/{dict_args['Name-Archive']}", "w+") as archive:
            for i in proxy_list:
                archive.write(f"{i}\n")

        filter_list = [i for i in proxy_list if i]
        return set(filter_list)