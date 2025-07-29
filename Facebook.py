from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome()
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()
# width = 1920
# height = 1080
# driver.set_window_size(width, height)
time.sleep(5)  # Wait for pop-up to load

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.click()
email.clear()
email.send_keys("7585831166")
time.sleep(1)

password = driver.find_element(By.XPATH, "//input[@type='password']")
password.clear()
password.send_keys("DoGesh$007")
time.sleep(3)

password_check = driver.find_element(By.XPATH, "//div[@class='_9lsa']")
for _ in range(2):
    password_check.click()
    time.sleep(2)
login = driver.find_element(By.XPATH, "//button[@name='login']").click()

                               


time.sleep(20)
driver.quit()


