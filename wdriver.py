import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome import service
from bs4 import BeautifulSoup as bss

webdriver_service = service.Service('/home/array/Downloads/operadriver_linux64/operadriver')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

myUserId = 'hack_it_like_you_know'
driver.get('https://instagram.com/')
cookie_file='cookie.data'
cookies = pickle.load(open(cookie_file, "rb"))
for i in cookies:
	driver.add_cookie(i)

driver.get('https://instagram.com/'+myUserId+'/followers')
driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()

followersPageSource = driver.page_source
soup = bss(followersPageSource, features='html.parser')

time.sleep(10)