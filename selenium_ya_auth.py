from selenium import webdriver
import unittest
import time
import json

'''
File secret.json required in app dir.
File format is dict with keys "login" and "pwd"

Copy appropriate selenium driver to app dir
'''
class UntitledTestCase(unittest.TestCase):

    def read_key(self):
        self.keyfile = 'secret.json'
        with open(self.keyfile, encoding='utf-8') as f:
            secret = json.load(f)
            self.login = secret.get("login", None)
            self.pwd = secret.get("pwd", None)

    def setUp(self):
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.read_key()

    def test_selenium_ya(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth")
        driver.find_element_by_name("login").send_keys(self.login)
        print(driver.find_element_by_css_selector(".button2_type_submit"))
        driver.find_element_by_css_selector(".button2_type_submit").click()
        driver.find_element_by_id("passp-field-passwd").send_keys(self.pwd)
        driver.find_element_by_css_selector(".passp-form-button").click()
        #============captcha manual input=============
        time.sleep(30)