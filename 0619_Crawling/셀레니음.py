from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "./chromedriver.exe"

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

#보통 객체를 만들어서 객체반환 받아서 쓰는데
url = "https://www.python.org/"
#url = "http://google.com"

driver.get(url)

#q라는 이름을 갖는 input 태그를 찾아온다
search_box = driver.find_element_by_name("q")

#Input 태그에 글자를 뿌린다. - 키보드 누름 정보를 보내라
# search_box.send_keys("크롤링")
search_box.send_keys("python")

#서버로 정보를 보내라
# search_box.submit() - form tag 문제가 있음

#submit이 안될때 또 다른 방법
search_box.send_keys(Keys.RETURN)


#스크린샷 찍기
driver.set_window_size(1400,1000)
driver.save_screenshot('test1.png')

#브라우저 닫기
driver.quit()
