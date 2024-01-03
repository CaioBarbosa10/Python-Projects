from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

#select_number = driver.find_element(By.CSS_SELECTOR,".hp-statistieken div p a")
#print(select_number)
#print(select_number.text)

#select_number.click()





driver.quit()
