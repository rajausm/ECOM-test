from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# test case 1 login for admin
driver.get('http://15.207.106.139/login.php')
driver.maximize_window()


#test case 2 invalid login
driver.find_element(By.XPATH, '//a[@href="login.php"]').click()


driver.find_element(By.XPATH, '//input[@name="Username"]').send_keys('asd')

driver.find_element(By.XPATH, '//input[@name="Password"]').send_keys('abc12345')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(2)
#test case 3 valid login
driver.find_element(By.XPATH, '//input[@name="Username"]').send_keys('raja')

driver.find_element(By.XPATH, '//input[@name="Password"]').send_keys('usman')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(3)
