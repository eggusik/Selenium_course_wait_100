import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
calc = lambda x:str(math.log(abs(12*math.sin(int(x)))))
try:
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x = calc(int(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])




except Exception as e:
    print(e.__class__.__name__)


finally:
    time.sleep(1)
    browser.quit()

