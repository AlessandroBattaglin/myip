# **My Public Ip**

## Code wrote by M4rt33
### [Youtube Channel](https://www.youtube.com/channel/UCp84qTAcb-1uQyr8Y3IInKQ?view_as=subscriber "Youtube Channel")
### [Telegram Contact](https://t.me/M4rt33 "Telegram Contact")

## How to install it:

```
git clone https://github.com/AlessandroBattaglin/myip.git

pip install -r requirements
```

### A great thank's to [MyIp.com](http://myip.com "MyIp.com")

[![MyIp Logo](https://www.myip.com/img/myip.png "MyIp Logo")](http://www.myip.com/img/myip.png "MyIp Logo")
**For letting me use their html code. Using bs4 (BeautifulSoup4) to scrape their data.**

## **Imports**


```python
import requests
from bs4 import BeautifulSoup
import time
import os
import sys
from colorama import Fore
```

## **Complete code**

```python
import requests
from bs4 import BeautifulSoup
import time
import os
import sys
from colorama import Fore


clear = lambda: os.system('cls')

product_url = requests.get('https://www.myip.com/')

def spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + '[*] Loading... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

def main():
	clear()
	spinner()
	clear()
	soup = BeautifulSoup(product_url.content, 'html.parser')
	price = soup.find(id="ip").get_text()
	country = soup.find(class_="info_2").get_text()
	site = soup.find(class_="pie").get_text()

	print(Fore.YELLOW + "+---------------------------------+" + Fore.RESET)
	print(Fore.LIGHTRED_EX + "Your IP address is: " + Fore.RESET + price)
	print(Fore.LIGHTRED_EX + "Country: " + Fore.RESET + country)
	print(Fore.YELLOW + "+---------------------------------+" + Fore.RESET)
	print()
	print("Thank's to: " + Fore.LIGHTRED_EX + site + Fore.RESET)

main()
```
<!--more-->

<!--more-->

<!--more-->

<!--more-->
