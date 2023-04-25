from Config.config import TestData
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    EMAIL_ID = "username"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_ID = "loginBtn"
    SIGNUP_LINK = "Sign up"

    def __int__(self, driver):
        self.driver = driver

    def get_login_page_title(self):
        page_title = self.driver.title

    def is_signup_link_exists(self):
        self.driver.find_element(By.LINK_TEXT, self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.driver.find_element(By.ID, self.EMAIL_ID).send_keys(username)
        self.driver.find_element(By.ID, self.PASSWORD_ID).send_keys(password)
        self.driver.find_element(By.ID, self.LOGIN_BUTTON_ID).click()




