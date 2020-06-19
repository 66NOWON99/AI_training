from selenium import webdriver
path = "./chromedriver.exe"

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

#보통 - 객체를 만들어서 객체반환받아서 쓰는데 

driver.get("http://google.com")

#q라는 이름을 갖는 input 태그를 찾아온다 
search_box = driver.find_element_by_name("q")

#input 태그에 글자를 뿌린다. - 키누름 정보를 보내라 
search_box.send_keys("크롤링")

#서버로 정보를 보내라 
search_box.submit()