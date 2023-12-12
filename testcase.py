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
driver.get('http://15.207.106.139/')
driver.maximize_window()

driver.find_element(By.XPATH, '//a[@class="dropdown-toggle"]').click()
driver.find_element(By.XPATH, '//a[@href="category.php?category=laptops"]').click()

driver.find_element(By.XPATH, '//a[@href="product.php?product=dell-inspiron-15-7000-15-6"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg btn-flat"]').click()
