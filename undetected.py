import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd
from time import sleep

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    webdriver = uc.Chrome(
        options=options,
    )
    webdriver.get('https://www.nombrerutyfirma.com/')
    sleep(4)
    for i in range(1,10):
        webdriver.get('https://www.nombrerutyfirma.com/')
        rut_b = webdriver.find_element(By.LINK_TEXT, value='RUT')
        rut_b.click()
        div_rut = webdriver.find_element(By.XPATH, value='//*[@id="formato-live"]/div/input')
        div_rut.click()
        div_rut.send_keys("18161379-3")
        buscar_b = webdriver.find_element(By.XPATH, value='//*[@id="formato-live"]/div/span/button').click()
    sleep(30)
