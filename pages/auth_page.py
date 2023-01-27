from .base_page import BasePage
from .locators import AuthLocators

import os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=22df6121-61b0-478a-8b6d-8e43ca95577d&theme=light&auth_type"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.input_field_user)
        self.phone = driver.find_element(*AuthLocators.input_field_user)
        self.passw = driver.find_element(*AuthLocators.input_field_pass)
        self.btn = driver.find_element(*AuthLocators.auth_btn)
        self.tab_phone = driver.find_element(*AuthLocators.tab_phone)
        self.tab_email = driver.find_element(*AuthLocators.tab_email)
        self.tab_login = driver.find_element(*AuthLocators.tab_login)
        self.tab_ls = driver.find_element(*AuthLocators.tab_ls)
        self.auth_form_title = driver.find_element(*AuthLocators.auth_form_title)
        self.check_box = driver.find_element(*AuthLocators.check_box)
        self.reg_link = driver.find_element(*AuthLocators.reg_link)

    def uncheck_box(self):
        self.check_box.click()

    def btn_click(self):
        self.btn.click()

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_email_click(self):
        self.tab_email.click()

    def tab_ls_click(self):
        self.tab_ls.click()

    def tab_login_click(self):
        self.tab_login.click()

    def reg_link_click(self):
        self.reg_link.click()
