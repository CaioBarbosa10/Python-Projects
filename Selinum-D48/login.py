from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME,"fName")
first_name_input.click()
first_name_input.send_keys("Caio")


last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.click()
last_name_input.send_keys("Barbosa")

email = driver.find_element(By.NAME,"email")
email.click()
email.send_keys("caiocbarbosa7@gmail.com")

btn = driver.find_element(By.CSS_SELECTOR,".form-signin button")
btn.click()



driver.quit()