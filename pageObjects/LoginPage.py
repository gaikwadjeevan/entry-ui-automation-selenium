from selenium import webdriver
from selenium.webdriver.common.by import By


class loginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "//input[@name='login']"
    link_MyAccount_xpath = "//a[normalize-space()='My Account']"
    link_Orders_linktext = "Orders"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickOrders(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Orders_linktext).click()
