from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
element = WebDriverWait(driver,5,0.5).until(expected_conditions.presence_of_all_elements_located((By.ID,'kw')))
driver.find_element_by_id('kw').send_keys('selenium')