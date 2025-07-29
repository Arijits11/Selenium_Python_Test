from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
# width = 1920
# height = 1080
# driver.set_window_size(width, height)
time.sleep(5)  # Wait for pop-up to load

try:
    continue_shopping = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button").click()
    time.sleep(3)
except:
    pass  # Element not found, move on

login_button = driver.find_element(By.XPATH, "//div[@id='nav-link-accountList']//a[contains(@class,'nav-progressive-attribute')]").click()
time.sleep(3)

email = driver.find_element(By.XPATH, "//input[@id='ap_email_login']").send_keys("asarkar918@gmail.com")
time.sleep(2)
continue_button = driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
time.sleep(2)
password = driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Asarkar@1998")
time.sleep(2)
sign_in = driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
time.sleep(3)




time.sleep(10)
driver.quit()
