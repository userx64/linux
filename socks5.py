#proxies socks5 parser and checker
import requests #pip3 install requests[socks]
import bs4
import sys
import os
from colorama import Fore, init
init(autoreset=True)



def check(ip, porta):
    try:
        r = requests.get("http://myexternalip.com/raw", proxies=dict(http="socks5://" + ip + ":" + porta), timeout=2)
        return True
    except requests.exceptions.ConnectionError:
        return False
    except requests.exceptions.ReadTimeout:
        return False
    except KeyboardInterrupt:
        print()
        sys.exit()

def save(proxy):
    try:
        for value in proxy:
            value = str(value)
            if value.isdecimal():
                porta = value
            elif len(value) != 2:
                ip = value

        if check(ip, porta):
            print(Fore.WHITE + "# " + ip + ":" + porta)
            with open(filename, "a") as f:
                for p in proxy:
                    f.write(str(p) + ":")
                f.write("\n")
        else:
            print(Fore.RED + "# " + ip + ":" + porta)
    except KeyboardInterrupt:
        print()
        sys.exit()

def isValue(string):
    try:
        if string.startswith("<td>"):
            string = string[4:-5] #ottieni una stringa pulita
        if string.count(".") == 3: #se ip
            i = 0
            sub = string.split(".")
            for s in sub:
                s = str(s)
                if not s.isdecimal():
                    i = 1
            if i == 0:
                return "ip", string
        if string.isdecimal(): #se porta
            return "port", int(string)
        if len(string) == 2:
            return "state", string
        return False, False
    except KeyboardInterrupt:
        print()
        sys.exit()

def parsing(html):
    try:
        soup = bs4.BeautifulSoup(html, "html.parser")
        elenco = soup.findAll("td")
        proxy = []
        i = 0
        for _ in elenco:
            _ = str(_)
            isvalue, value = isValue(_)
            if isvalue:
                proxy.append(value)
                if len(proxy) == 3:
                    i += 1
                    save(proxy)
                    proxy = []
    except KeyboardInterrupt:
        print()
        sys.exit()
def request():
    return requests.get(host)
def myip():
    return requests.get("http://myexternalip.com/raw").text
if __name__ == "__main__":
    host = "https://www.socks-proxy.net"
    if len(sys.argv) != 2:
        print("Uso: python3 " + str(sys.argv[0]) + " <file>")
        sys.exit()
    filename = sys.argv[1]
    print(Fore.WHITE + "# Il tuo ip è: " + myip())
    response = request()
    parsing(response.text)


