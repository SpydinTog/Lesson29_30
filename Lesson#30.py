import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://test.mensa.no/')
driver.maximize_window()
xpath_button_18_50 = '//button[contains(@class,"ageselect_1850")]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_18_50)))
button_18_50 = driver.find_element('xpath', xpath_button_18_50)
button_18_50.click()


id_start = 'startTest'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', id_start)))
button_start = driver.find_element('id', id_start)
button_start.click()
time.sleep(0.5)

d = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in d:
    xpath_q_b = f'//div[@id="question_{number}"]//div[@data-answerid="0"]'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q_b)))
    q_b = driver.find_element('xpath', xpath_q_b)
    q_b.click()
    time.sleep(0.5)

