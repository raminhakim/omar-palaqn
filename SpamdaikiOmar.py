import requests
from time import sleep
import webbrowser
import random
import requests
import json
from secrets import token_hex
import secrets
import os
import sys
import uuid
from uuid import uuid4
from time import sleep
import webbrowser
import time
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
os.system("clear")

r = requests.session()
print(Z+' \n - - - - - - - - - - - - - - - - - - -  \n')
token = input(X+"- ENTER TOKEN BOT: "+Y)
ID = input(X+"- ENTER ID Tele : "+Y)
print(B+' \n - - - - - - - - - - - - - - - - - - -  \n')
ABS      = input(F+' [1] Enter message : ')
JJ9MJ = input(' [2] Enter message : ')
ABS3    = input(' [3] Enter message : ')
MSG4   = input(' [4] Enter message : ')
print(B+' \n - - - - - - - - - - - - - - - - - - -  \n')
done = 1
while True:
	a = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ABS}').text
	a2 = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={JJ9MJ}').text
	
	a3 = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ABS3}').text
	
	a4 = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={MSG4}').text
	

	print(f'{done} DON MSG TELE BOT  ✅')
	done +=1

