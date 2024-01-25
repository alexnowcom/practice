from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com')
formField = driver.find_element_by_xpath('//*[@id="APjFqb"]')
formField.send_keys('Hello World')
submitButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
submitButton.click()