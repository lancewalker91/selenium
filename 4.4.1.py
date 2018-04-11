from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver =  webdriver.Firefox()
driver.get('https://www.yunke.com')
right_click =driver.find_element_by_xpath('//*[@id="site_nav"]/li[2]/a')
ActionChains(driver).context_click(right_click).perform()
driver.quit()