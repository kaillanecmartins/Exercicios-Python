import urllib
import urllib.request

try:
   site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[0; 31; 0mSite não encontrado \033[m')
else:
    print('\033[0; 33; msite encontrado com sucesso!\033[m')
