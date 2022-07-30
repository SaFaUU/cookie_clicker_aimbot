from cffi.backend_ctypes import long

WEBSITE_URL = "http://orteil.dashnet.org/experiments/cookie/"
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

TIMEOUT = 5
DRIVER_PATH = "C:/Selenium/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()),
                          executable_path=DRIVER_PATH)
driver.get(WEBSITE_URL)
cookie = driver.find_element(By.ID, "cookie")


def click():
    time_start = time.time()
    while time.time() < time_start + TIMEOUT:
        cookie.click()


while True:
    click()
    money = driver.find_element(By.ID, "money").text
    print(money)
    if long(money) > 123456789:
        buy_item = driver.find_element(By.ID, "buyTime machine")
        buy_item.click()
    elif long(money)  > 1000000:
        buy_item = driver.find_element(By.ID, "buyPortal")
        buy_item.click()
    elif long(money)  > 50000:
        buy_item = driver.find_element(By.ID, "buyAlchemy lab")
        buy_item.click()
    elif long(money)  > 7000:
        buy_item = driver.find_element(By.ID, "buyShipment")
        buy_item.click()
    elif long(money)  > 2000:
        buy_item = driver.find_element(By.ID, "buyMine")
        buy_item.click()
    elif long(money)  > 500:
        buy_item = driver.find_element(By.ID, "buyFactory")
        buy_item.click()
    elif long(money) > 100:
        buy_item = driver.find_element(By.ID, "buyGrandma")
        buy_item.click()
    elif long(money) > 15:
        buy_item = driver.find_element(By.ID, "buyCursor")
        buy_item.click()
    cookie_per_second = driver.find_element(By.ID, "cps")
    print(cookie_per_second.text)