from selenium import webdriver
driver = webdriver.Firefox()
first_url = 'https://www.baidu.com'
print('now access {}'.format(first_url))
driver.get(first_url)
second_url = 'https://news.baidu.com'
print('now access {}'.format(second_url))
driver.get(second_url)
print('back to {}'.format(first_url))
driver.back()
print('forward to {}'.format(second_url))
driver.forward()
driver.quit()