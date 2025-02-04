from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()
time.sleep(4)
driver.quit()