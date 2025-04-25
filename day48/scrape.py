from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://google.com")

text = driver.find_element(By.CLASS_NAME, "RNmpXc").get_attribute("value")
print(text)

driver.quit()
