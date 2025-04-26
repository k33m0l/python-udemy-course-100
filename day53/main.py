from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import pandas

driver = webdriver.Firefox()
driver.get("https://appbrewery.github.io/Zillow-Clone/")

def clean_up_address(address: str):
    return address.replace(" | ", " ")

def listing_to_dict(listing: WebElement):
    url = listing.find_element(By.CLASS_NAME, "StyledPropertyCardDataArea-anchor").get_attribute("href")
    cost = listing.find_element(By.CLASS_NAME, "PropertyCardWrapper__StyledPriceLine").text.split("/")[0].split("+")[0]
    address = listing.find_element(By.TAG_NAME, "address").text
    return {
        "url": url,
        "cost": cost,
        "address": clean_up_address(address)
    }

def save(listings):
    df = pandas.DataFrame(listings)
    df.to_csv("results.csv")
    

listings = driver.find_elements(By.CLASS_NAME, "ListItem-c11n-8-84-3-StyledListCardWrapper")
listings = [listing.find_element(By.CLASS_NAME, "StyledPropertyCardDataWrapper") for listing in listings]
listings = [listing_to_dict(listing) for listing in listings]

save(listings)
driver.quit()
