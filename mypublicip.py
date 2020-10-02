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