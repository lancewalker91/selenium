from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://m.mail.10086.cn')
print('kaungaoixianshi ')
#driver.maximize_window()
driver.set_window_size(480,800)
driver.quit()