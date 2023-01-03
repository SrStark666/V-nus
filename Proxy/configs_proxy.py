import requests
import re

def proxy_(save: str) -> list[dict[str: int]]: #list: [dict{http://127.0.0.1:80, https://127.0.0.1:80}]
    valid_proxys = []
    get = requests.get("https://free-proxy-list.net/")
    html = get.text
    html = html.split("UTC."); html = html[1].split("</")
    proxy_list = html[0].split("\n")

    if save != "1" and not re.search(".txt", save):
        save = save + ".txt"

    for i in proxy_list:
        if i != "":
            proxy = i.replace("\n", "").split(":")[0]
            port = i.replace("\n", "").split(":")[1]

            dict_ = {"http": f"http://{proxy}:{port}",
                "https": f"https://{proxy}:{port}"}

            valid_proxys.append(dict_)

    if '1' in save:
        with open("Proxy/proxy_list.txt", "w+") as archive:
            for i in proxy_list:
                archive.write(f"{i}\n")

    filter_list = [i for i in proxy_list if i]
    return set(filter_list)
