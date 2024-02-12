import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.google.com')

except :
    print("Site Não Acessivel.:")
else:
    print('Site Acessivel')