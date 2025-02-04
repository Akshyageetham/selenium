from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/guviofficial/')
time.sleep(5)
print(driver.current_url)
followers_element = driver.find_element(By.XPATH, "//*[contains(text(), 'followers')]").text
time.sleep(5)
print(followers_element)
following_element = driver.find_element(By.XPATH, "//*[contains(text(), 'following')]").text
time.sleep(5)
print(following_element)
followers_count = followers_element.get_attribute("title")
following_count = following_element.text
print(f"Followers: {followers_count}"),
print(f"Following: {following_count}")

driver.quit()




