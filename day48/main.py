import time
import datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# chrome_driver_path = "chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("http://orteil.dashnet.org/experiments/cookie/")

# cookie = driver.find_element(By.ID,'cookie')
# cookie.click()

time_execution = 300   # [seconds]
initial_time = time.time()
timeout = initial_time + time_execution


while time.time() != timeout:
    time_now = 0
    if time.time() == initial_time + 5:
        time_now = 