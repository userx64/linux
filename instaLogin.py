#solo funzione Login
import requests
import json
from getpass import getpass
import sys

def Login(username, password):
    with requests.Session() as s:
        s.cookies.update({'sessionid' : " ", "mid" : " ", "ig_pr" : "1", "ig_vw" : '1920', 'csrftoken' : " ",  's_network' : " ", 'ds_user_id' : " "})
        s.headers.update({
                    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'x-instagram-ajax':'1',
                    'X-Requested-With': 'XMLHttpRequest',
                    'origin': 'https://www.instagram.com',
                    'ContentType' : 'application/x-www-form-urlencoded',
                    'Connection': 'keep-alive',
                    'Accept': '*/*',
                    'Referer': 'https://www.instagram.com',
                    'authority': 'www.instagram.com',
                    'Host' : 'www.instagram.com',
                    'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
                    'Accept-Encoding' : 'gzip, deflate'
            })
        r = s.get("https://www.instagram.com/")
        s.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})
        data = {'username':username, 'password':password}
        r = s.post('https://www.instagram.com/accounts/login/ajax/', data=data)
        token = r.cookies.get_dict()['csrftoken']
        s.headers.update({'X-CSRFToken' : token})
        return json.loads(r.text)
if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
    else:
        username = input("Username: ")
        password = getpass("Password: ")
    print(Login(username, password))
