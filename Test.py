import requests
# import beautifulsoup4 2系でのみ動作？
import lxml.html


def CallRequests():
    r = requests.get('https://www.google.co.jp/')
    print(r.status_code)

'''
実行時にエラーが出る
def CallLxml():
    root = lxml.html.parse('https://www.google.co.jp/').getroot()
    print(root.cssselect('title')[0].text)
'''

if __name__ == '__main__':
    CallRequests()
    CallLxml()
