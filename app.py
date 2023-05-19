from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://medium.com/")

time.sleep(5)

#nav_elem = driver.find_element(By.CSS_SELECTOR, '#scroller-items > div.fg.iw.bx.ir.s > a > p > span > button > font > font')
#ActionChains(driver).click(nav_elem).perform()
#time.sleep(5)

article = driver.find_element(By.CSS_SELECTOR, '#root > div > div.n.dc > div.ej.ah.ia.ib.ic > div.n.p > div > div > section > div > div > div.kg.kh.ah > div:nth-child(3) > div > div > div > a > h2')
ActionChains(driver).click(article).perform()
time.sleep(15)

