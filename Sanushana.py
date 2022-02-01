import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromedriver = webdriver.Chrome ("/Users/sanushanak/Downloads/chromedriver-1")
chromedriver.get("https://www.facebook.com") #A
chromedriver.maximize_window()
print("I am displaying" + chromedriver.title)
usernameTxtBox = chromedriver.find_element(By.ID, "email")
passwordTxtBox = chromedriver.find_element(By.ID, "pass")
logInBtn = chromedriver.find_element(By.NAME, "login")
usernameTxtBox.send_keys("shanu.29@hotmail.com") #Enter your facebook username
passwordTxtBox.send_keys("hdhsiubda") #Enter your facebook password
logInBtn.click()

time.sleep(5)
