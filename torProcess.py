import requests
import stem.process
import sys


def networking():
    pass #inserisci il tuo codice...

def checktor():
    html = requests.get("http://check.torproject.org/", proxies=proxies).text
    if "Sorry. You are not using Tor." in html:
        return False
    return True

def myip():
    global proxies
    proxies = {"http":"socks5://127.0.0.1:" + socksPort, "https":"socks5://127.0.0.1:"+socksPort, "ftp":"socks5://127.0.0.1:"+socksPort}
    return requests.get("http://myexternalip.com/raw", proxies=proxies).text
def uso():
    print("Uso: python3 %s <porta> <nazione>" % sys.argv[0])
    print("[!] La nazione deve essere lunga due caratteri [!]")
    print("Esempio: python3 %s 4444 US" % sys.argv[0])
    sys.exit()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        uso()
    if not sys.argv[1].isdecimal() or len(sys.argv[2]) != 2:
        uso()
    socksPort = sys.argv[1]
    nazione = sys.argv[2]
    print("Tentando una connessione verso Tor...")
    tor = stem.process.launch_tor_with_config( config = {
        "SocksPort" : socksPort, "ExitNodes": "{" + nazione + "}",
    })
    print("Il tuo ip è: " + str(myip())[:-1])
    if checktor():
        print("Stai usando Tor!")
    else:
        print("Fatal: non stai usando Tor..")
    tor.kill()


