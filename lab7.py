from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from authoptions import account_mail, account_password

driver = webdriver.Chrome(executable_path="D:\\python-selenium\\chromedriver\\chromedriver.exe")
driver.get("https://onlinegdb.com/")

driver.find_element(By.XPATH, "//*[@id=\"login_logout_span\"]/a").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(account_mail)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(account_password)

driver.find_element(By.ID, "login-submit").click()

driver.find_element(By.XPATH, "//*[@id=\"left-component\"]/div[2]/div[1]/a[1]").click()

time.sleep(10)

driver.quit()