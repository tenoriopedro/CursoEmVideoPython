import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('\033[31mO site não esta acessivel.\033[m')
else:
    print('\033[32mO site esta acessivel.\033[m')