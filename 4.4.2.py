from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('https://www.yunke.com/index.main.login')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[1]/div[2]/input').send_keys('17600117243')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').send_keys('117243')
driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[2]/input').submit()
#driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/ul[2]/li[1]/form/div[4]/input').click()
#time.sleep(5)
#driver.refresh()
'''
driver.get('https://litao.yunke.com/org.main.template#bottom')
test = driver.find_element_by_xpath('//*[@id="template-course-data"]/div/form/div[3]/div/span[2]/a')
test.click()
element = driver.find_element_by_xpath('//*[@id="template-course-data"]/div/form/div[3]/dl/dd[10]/div/img')
target = driver.find_element_by_xpath('//*[@id="template-course-data"]/div/form/div[3]/dl/dd[1]/div/img')
ActionChains(driver).drag_and_drop(element,target).perform()
'''
#WebDriverWait(driver,1,0.5).until(expected_conditions.presence_of_all_elements_located((By.ID,'chick-down-show')))
above = driver.find_element_by_id('chick-down-show')
ActionChains(driver).move_to_element(above).perform()
#driver.quit()
