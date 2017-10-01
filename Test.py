import requests
import lxml


def Func():
    r = requests.get('https://www.google.co.jp/')
    print(r.status_code)

if __name__ == '__main__':
    Func()
