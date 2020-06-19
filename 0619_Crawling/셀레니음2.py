from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "./chromedriver.exe"

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

#보통 객체를 만들어서 객체반환 받아서 쓰는데
url = "https://www.w3schools.com/colors/colors_rgb.asp"
driver.get(url)

import time
time.sleep(2)
#id를 통해서 객체에 접근해야 한다
# color1 = driver.find_element_by_css_selector("#r01").send_keys("80")
# color2 = driver.find_element_by_css_selector("#g01").send_keys("55")
# color3 = driver.find_element_by_css_selector("#b01").send_keys("25")

from bs import BeautifulSoup 
html = driver.page_source
print(html)
bs = BeautifulSoup(html)
color = bs.find("div", {"id":"hex01"})
print(color.text)

######
# color1 = driver.find_element_by_id("r01")
# color2 = driver.find_element_by_id("g01")
# color3 = driver.find_element_by_id("b01")

# color1.send_keys("255")
# color2.send_keys("50")
# color3.send_keys("20")




# print(color1.text)

#브라우저 닫기
# driver.quit()
