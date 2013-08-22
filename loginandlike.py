from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Loginandlike(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.influenster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_loginandlike(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("signin_username").send_keys("asd")
        driver.find_element_by_id("signin_password").send_keys("vokal1980")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("OK").click()
        driver.find_element_by_id("signin_username").clear()
        driver.find_element_by_id("signin_username").send_keys("")
        driver.find_element_by_id("signin_password").clear()
        driver.find_element_by_id("signin_password").send_keys("")
        driver.find_element_by_id("signin_username").send_keys("onder")
        driver.find_element_by_id("signin_password").send_keys("qweqweqweqw")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("OK").click()
        driver.find_element_by_id("signin_username").clear()
        driver.find_element_by_id("signin_username").send_keys("")
        driver.find_element_by_id("signin_password").clear()
        driver.find_element_by_id("signin_password").send_keys("")
        driver.find_element_by_id("signin_password").send_keys("vokal1980")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("OK").click()
        driver.find_element_by_id("signin_password").clear()
        driver.find_element_by_id("signin_password").send_keys("")
        driver.find_element_by_id("signin_username").send_keys("onder")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("OK").click()
        driver.find_element_by_id("signin_username").clear()
        driver.find_element_by_id("signin_username").send_keys("")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("OK").click()
        driver.find_element_by_id("signin_username").send_keys("onder")
        driver.find_element_by_id("signin_password").send_keys("vokal1980")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("Reviews").click()
        driver.find_element_by_css_selector("input.search_text").click()
        driver.find_element_by_css_selector("input.search_text").send_keys("palmolive")
        driver.find_element_by_xpath("//a[contains(@href, '/review/palmolive-soft-touch')]").click()
        driver.find_element_by_id("qatab").click()
        driver.find_element_by_id("pictab").click()
        driver.find_element_by_id("videotab").click()
        driver.find_element_by_id("reviewtab").click()
        driver.find_element_by_id("upcaretimg").click()
        driver.find_element_by_id("upcaretimg").click()
        driver.find_element_by_id("downcaretimg").click()
        driver.find_element_by_id("downcaretimg").click()
        driver.find_element_by_id("downcaretimg").click()
        driver.find_element_by_id("upcaretimg").click()
        driver.find_element_by_css_selector("i.icon-flag.opa50").click()
        driver.find_element_by_name("flagreviewreasonfrm").click()
        driver.find_element_by_link_text("Flag").click()
        driver.find_element_by_css_selector("i.icon-flag.opa50").click()
        driver.find_element_by_css_selector("i.icon-flag.opa50").click()
        driver.find_element_by_css_selector("i.icon-flag.opa50").click()
        driver.find_element_by_css_selector("button.btn.dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
