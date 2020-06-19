from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

path = "./chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(path, chrome_options=options)

driver.implicitly_wait(3)

#보통 - 객체를 만들어서 객체반환받아서 쓰는데 
url = "https://www.w3schools.com/colors/colors_rgb.asp"
driver.get(url)

import time
time.sleep(2)
#id를 통해서 객체에 접근해야 한다 
a = driver.find_element_by_id("r01").send_keys(50)
#driver.find_element_by_css_selector("#g01").send_keys(50)
#driver.find_element_by_css_selector("#b01").send_keys(70)
from bs4 import BeautifulSoup
html = driver.page_source
#print(html)
bs = BeautifulSoup(html)
color = bs.find("div", {"id":"hex01"})
print(color.text)

#브라우저 닫기
