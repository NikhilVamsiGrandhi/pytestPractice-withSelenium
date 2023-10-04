from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://github.com/login")

# Find the username and password input fields and the login button
time.sleep(2)
driver.find_element(By.ID,"login_field").send_keys("nikhil.grandhi@kanerika.com")
time.sleep(2)
driver.find_element(By.ID,'password').send_keys("Nikhil@5775")
driver.find_element(By.NAME,'commit').click()

driver.maximize_window()
name_obj=driver.title

if name_obj=="GitHub":
    print('login is succesfull')
else:
    print("login fail")

time.sleep(3)
# driver.quit()