from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.by import By
import time
driver = webdriver.Chrome(service=ChromeDriverManager().install())

driver.get("https://www.homedepot.ca")
search_box = driver.find_element(By.ID, "id7597")
search_box.send_keys("Milwaukee Drilling machine")
search_box.send_keys(Keys.ENTER)



time.sleep(30)

driver.close()

driver.quit()