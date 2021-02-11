import os
from os.path import join, dirname

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

WP_ADMIN_USER = os.environ.get('WP_ADMIN_USER')
WP_ADMIN_PASS = os.environ.get('WP_ADMIN_PASS') 

 
driver = webdriver.Chrome(executable_path="./chromedriver")

url = 'http://wptest1.local/wp-login.php'
 

# 操作
driver.get(url)

element = driver.find_element_by_id('user_login')
element.send_keys(WP_ADMIN_USER)

element = driver.find_element_by_id('user_pass')
element.send_keys(WP_ADMIN_PASS)


element.send_keys(Keys.ENTER)