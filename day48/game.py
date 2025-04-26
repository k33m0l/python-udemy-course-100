from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

MAX_CLICK_COUNT = 10000000

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

wait_for_consent = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[Exception])
wait_for_consent.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fc-primary-button p"))).click()

lang_select_div = driver.find_element(By.ID, "langSelect-EN").click()

wait_for_cookie = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[Exception])
cookie = wait_for_cookie.until(expected_conditions.visibility_of_element_located((By.ID, "bigCookie")))

def get_unlocked_upgrades():
    return driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

for click in range(0, MAX_CLICK_COUNT):
    try:
        upgrades = get_unlocked_upgrades()
        if len(upgrades) > 0:
            upgrades[0].click()
    except Exception as error:
        pass
        # Silenty swallowing error
    cookie.click()

driver.quit()
