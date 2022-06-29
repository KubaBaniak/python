from click import option
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import chromedriver_binary

url = 'https://allegro.pl/oferta/lego-creator-10295-porsche-911-10874961606?bi_s=ads&bi_m=productlisting%3Adesktop%3Aquery&bi_c=ZjBhYWZiNjktMzBiZi00MGVkLTg4ODAtNjVjNjE2MTQyMmExAA&bi_t=ape&referrer=proxy&emission_unit_id=c07dc4d5-44b6-4cba-98de-d1eccc608cc7'

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = wd.Chrome(options=options)
wd.implicitly_wait(10)
wd.get(url)

privacy_button = wd.find_element(by=By.XPATH, value='//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div[2]/button[1]').click()
input()
buy_now = wd.find_element(by=By.XPATH, value='//*[@id="buy-now-button"]').click()
# Log into your account:
email_field = wd.find_element(by=By.XPATH, value='//*[@id="login"]').send_keys('kuba121201@gmail.com')
password_field = wd.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('Kosteczka123')
login_button = wd.find_element(by=By.XPATH, value='//*[@id="authForm"]/div/div/div[2]/button').click()

payment_method = wd.find_element(by=By.XPATH, value='//*[@id="payment-soap-blik-1-label"]').click()

buy = wd.find_element(by=By.XPATH, value='//*[@id="buy-and-pay-btn"]')
buy.click()

card_id = wd.find_element(by=By.XPATH, value='//*[@id="blik-token"]')