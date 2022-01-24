#coding=utf8
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import threading
import time
import ctypes, sys,os



def req_http(http_list_one,ip):
    res = requests.get(url=http_list_one)
    soup = BeautifulSoup(res.text,'lxml')
    a = http_list_one.split('/')[4]
    for item in soup.find('ul',attrs={'class':'comma-separated'}).children:
        ip.append((item.string + ' ' + a + '\n'))
    
def read_host(ip):
    path = "C:\Windows\System32\drivers\etc"
    fil = "hosts"
    cmd = "/c ipconfig /flushdns"
    new_hosts = []
    os.chdir(path)
    try:
        f = open("hosts","r+",encoding="utf-8")
    except:
        pass
    
    try:
        for x in f.readlines():
            if "github" in x:
                pass
            else:
                new_hosts.append(x)
    except:
        pass
    f.close()
    for x in ip:
        new_hosts.append(x)
    try:
        f = open("hosts","w+",encoding="utf-8")
    except:
        pass
    for x in new_hosts:
        f.write(x)
    f.close()
    
    ctypes.windll.shell32.ShellExecuteW(None, "open", "cmd.exe", cmd, None, 1)
    
    
def req_ip():
    http_list=['https://ipaddress.com/website/github.com',
               'https://ipaddress.com/website/assets-cdn.github.com',
               'https://ipaddress.com/website/github.global.ssl.fastly.net',
               'https://ipaddress.com/website/user-images.githubusercontent.com',
               'https://ipaddress.com/website/github.githubassets.com',
               'https://ipaddress.com/website/avatars.githubusercontent.com',
               'https://ipaddress.com/website/api.github.com',
               'https://ipaddress.com/website/api.github.com']
    th = []
    ip = []
    ip.append("#github begin\n")
    for x in http_list:
        t = threading.Thread(target=req_http,args=(x,ip,))
        t.start()
        th.append(t)
    for x in th:
        x.join()
    ip.append("#github end\n")
    return ip
    

if __name__=='__main__':

    if ctypes.windll.shell32.IsUserAnAdmin():
        print("正在获取github host...")
        ip = req_ip()
        read_host(ip)
        print("完成，5秒后自动关闭")
        time.sleep(5)
        
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


    
