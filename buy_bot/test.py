from click import option
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import random
import pickle

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

url = 'https://allegro.pl/oferta/lego-creator-10295-porsche-911-10874961606?bi_s=ads&bi_m=productlisting%3Adesktop%3Aquery&bi_c=ZjBhYWZiNjktMzBiZi00MGVkLTg4ODAtNjVjNjE2MTQyMmExAA&bi_t=ape&referrer=proxy&emission_unit_id=c07dc4d5-44b6-4cba-98de-d1eccc608cc7'

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

wd = wd.Chrome(options=options)


wd.implicitly_wait(10)
wd.get(url)

privacy_button = wd.find_element(by=By.XPATH, value='//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div[2]/button[1]')
privacy_button.click()

buy_now = wd.find_element(by=By.XPATH, value='//*[@id="buy-now-button"]')
buy_now.click()

# Log into your account:

email_field = wd.find_element(by=By.XPATH, value='//*[@id="login"]')
password_field = wd.find_element(by=By.XPATH, value='//*[@id="password"]')
login_button = wd.find_element(by=By.XPATH, value='//*[@id="authForm"]/div/div/div[2]/button')

email_field.send_keys('kuba121201@gmail.com')
password_field.send_keys('Kosteczka123')
login_button.click()

payment_method = wd.find_element(by=By.XPATH, value='//*[@id="payment-soap-blik-1-label"]')
payment_method.click()

# wd.find_element(by=By.XPATH, value='//*[@id="card-number"]')


buy = wd.find_element(by=By.XPATH, value='//*[@id="buy-and-pay-btn"]')
buy.click()

card_id = wd.find_element(by=By.XPATH, value='//*[@id="blik-token"]')
card_id.send_keys('123456')
# valid_thru = wd.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div/span/span/input')
# valid_thru.send_keys('523')

# cvv = wd.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div/span/span/input')
# valid_thru.send_keys('430')

# use_once_button = wd.find_element(by=By.XPATH, value='//*[@id="useButton"]')
# use_once_button.click()


input()

# add_to_cart_button = wd.find_element_by_xpath('//*[@id="add-to-cart-button"]')

# print(add_to_cart_button)

# add_to_cart_button.click()

# go_to_the_cart = wd.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div/div[3]/a')

# letyshops_button = wd.find_element_by_xpath('/html/app-content//app-notification/div/div[3]/div[3]/a/div')

# print(letyshops_button)

# go_to_the_cart.click()