from click import option
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import chromedriver_binary
import datetime
import time

url = 'https://allegro.pl/oferta/lego-creator-10295-porsche-911-10874961606?bi_s=ads&bi_m=productlisting%3Adesktop%3Aquery&bi_c=ZjBhYWZiNjktMzBiZi00MGVkLTg4ODAtNjVjNjE2MTQyMmExAA&bi_t=ape&referrer=proxy&emission_unit_id=c07dc4d5-44b6-4cba-98de-d1eccc608cc7'

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = wd.Chrome(options=options)
wd.implicitly_wait(10)
wd.get(url)

privacy_button = wd.find_element(by=By.XPATH, value='//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div[2]/button[1]').click()

menu = wd.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/header/div[1]/nav/div[5]/button').click()

login = wd.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/header/div[1]/nav/div[5]/div/div/div/div/div/a')
login.click()



# Log into your account:
email_field = wd.find_element(by=By.XPATH, value='//*[@id="login"]').send_keys('kuba121201@gmail.com')
password_field = wd.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('Kosteczka123')
login_button = wd.find_element(by=By.XPATH, value='//*[@id="authForm"]/div/div/div[2]/button').click()

# (year, month, day, hour, minute, second, milisecond)
start_date=datetime.datetime(2022, 5, 27, 20, 10, 15, 0)

while True:
    time.sleep(1)
    if datetime.datetime.now() >= start_date:
        wd.refresh()
        buy = wd.find_element(by=By.XPATH, value='//*[@id="one-click-buy-button"]').click()
        break

input()