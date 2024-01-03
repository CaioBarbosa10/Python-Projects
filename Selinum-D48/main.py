from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")



event_time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")

event_text = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

event = {}
for n in range(len(event_time)):
    event[n] = {
        "time": event_time[n].text,
        "name": event_text[n].text
    }
print(event)



driver.quit()


