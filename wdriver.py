import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from bs4 import BeautifulSoup as bss

webdriver_service = service.Service('/home/array/Downloads/operadriver_linux64/operadriver')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get('https://instagram.com/accounts/login')
time.sleep(2)
userText = driver.find_element_by_name("username")
userText.send_keys('hack_it_like_you_know\t')
input("this is the time you enter password and press enter ")
notnow = driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/div/button""")
notnow.click()
driver.find_element_by_xpath("""/html/body/div[4]/div/div/div/div[3]/button[2]""").click()
driver.get("https://www.instagram.com/hack_it_like_you_know/followers")
driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()
followersPageSource = driver.page_source
soup = bss(followersPageSource, features='html.parser')
