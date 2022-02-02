import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://bestbuy.ca")
actns = ActionChains(driver)

shop = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/header/div/div/div[2]/div/div/div/div/div/ul/li[1]/div/button/span")
shop.click()
time.sleep(5)
app = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/header/div/div/div[2]/div/div/div/div/div/ul/li[1]/div/div[2]/div/ul/li[3]/a")
actns.move_to_element(app).perform()
time.sleep(2)
mac = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/header/div/div/div[2]/div/div/div/div/div/ul/li[1]/div/div[2]/div/div[3]/div[2]/div[1]/ul/li[3]/a")
mac.click()
time.sleep(5)