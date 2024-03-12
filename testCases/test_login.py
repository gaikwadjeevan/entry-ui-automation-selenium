import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import loginPage
from testCases.conftest import project_root
from utilities.readProperties import readConfig
from utilities.customLogger import logGen


class Test_001_Login:
    url = readConfig.getURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGen.getLogGen()

    def test_login(self, setup):
        self.logger.info("******* Verifying Login functionality and Order Link TC001 ******")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = loginPage(self.driver)
        self.lp.clickMyAccount()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickOrders()

        actual_title = self.driver.title

        expected_title = "My Account – Automation Practice Site"
        if actual_title == expected_title:
            assert True
            self.driver.close()
            self.logger.info("******* OrderLink TC is Passed ******")
        else:
            self.driver.save_screenshot(f"{project_root}/screenshots/test_login.png")
            self.driver.close()
            self.logger.info("******* OrderLink Test Case is Failed ******")
            assert False


