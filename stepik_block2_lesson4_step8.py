import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

button_submit = browser.find_element_by_css_selector("#book")
button_submit.click()

x = browser.find_element_by_css_selector("#input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

input_math = browser.find_element_by_css_selector("input")
input_math.send_keys(y)

button_submit = browser.find_element_by_css_selector("#solve")
button_submit.click()

time.sleep(5)
browser.quit()
