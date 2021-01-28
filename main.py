from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen as req
import re
from pandas import DataFrame
import pandas
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

import requests

from bs4 import BeautifulSoup as Soup
import hashlib 


basicUrl = 'http://dt.data1688.com'

requ = Request(basicUrl, headers={'User-Agent': 'Mozilla/5.0'})
uClient = req(requ)
pageHtml = uClient.read()
uClient.close()
page_soup = soup(pageHtml, "html.parser")
##h888888
##yixunhui

with open('result_page.html', 'w', encoding='utf-8' , errors='ignore') as f: 
    print(page_soup)
    print(type(page_soup))
    f.write(page_soup.text)

def get_md5(s): 
	return hashlib.md5(bytes(s, encoding = 'utf8')).hexdigest()
def main():

	url = 'https://sevashoes.com/en/login'
	with requests.session() as session: 
		response = session.get(basicUrl)
		
		soup = Soup(response.text, 'lxml')
		challenge = soup.find('input' , id = 'challenge').get('value')
		headerStr = username + ':'+ get_md5(password)+':'+challenge
		result = get_md5(headerStr)
		data ={ 'username':username, 
				'password':'',
				'challenge':'',
				'response':result }

		response = session.post(url, data=data)
		print(response.text)

		with open('result_page.html', 'w', encoding='utf-8' , errors='ignore') as f: 
			f.write(response.text)





