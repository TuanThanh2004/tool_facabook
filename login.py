import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from webdriver_manager.chrome import ChromeDriverManager

def login(email, password):
    # chrome = r"D:\post_facebook\chromedriver-win64\chromedriver.exe"
    facebook_url = "https://www.facebook.com"
    # service = Service(chrome)
    # #
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_window_size(1000, 800)
    driver.set_window_position(10, 10)

    driver.implicitly_wait(5)

    time.sleep(random.randint(3, 5))
    driver.get(facebook_url)

    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)

    time.sleep(random.randint(8, 10))

    return driver
