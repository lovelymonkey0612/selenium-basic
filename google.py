import time

from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')
print(driver.title)
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element('name', 'q')
print(driver.current_url)
search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()