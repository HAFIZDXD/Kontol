import os

cookie=input('MASUKAN COOKIE :')
open('.cookie.txt','w').write(cookie)
os.system('python aorec.py')
