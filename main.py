from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from encryption import text

username = text.encode(input('What is your username: '))
password = text.encode(input('What is your password: '))

file = open('encryption.txt','a').write('\n'+str(username)+'\n'+str(password))

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://google.com')
