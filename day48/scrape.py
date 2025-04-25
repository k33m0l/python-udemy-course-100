from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li")

events = {}
for index in range(0, len(elements)):
    event_title = elements[index].find_element(By.TAG_NAME, "a").text
    event_date = elements[index].find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    events[index] = {
        "time": event_date,
        "name": event_title
    }

print(events)

driver.quit()
