from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.yunke.com/index.main.login')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').send_keys('17600117243')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').send_keys('117243')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').submit()
driver.get('https://www.yunke.com/index.user.uploadPic/1')
driver.find_element_by_xpath('//*[@id="browse"]').click()
os.system(r'C:\Users\Administrator\Desktop\upfile1.exe')
driver.find_element_by_xpath('//*[@id="up-save"]').click()
driver.quit()
