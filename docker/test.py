from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://85.193.92.39:4444/wd/hub',
options=options
)

driver.maximize_window()
driver.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
driver.find_element(By.CSS_SELECTOR, "#login_form")

driver.close()
driver.quit()

while True:
print("Test Execution Successfully Completed!")
time.sleep(1)
