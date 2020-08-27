import time

from selenium import webdriver
from selenium.webdriver.chrome import service


webdriver_service = service.Service('/home/array/Downloads/operadriver_linux64/operadriver')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get('https://www.google.com/')
input_txt = driver.find_element_by_name('q')
input_txt.send_keys('flipkart smartphones\n')

