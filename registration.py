from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Registration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/vokaladmin/Downloads/chromedriver')
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://testsrv.influenster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registration(self):
        driver = self.driver
        driver.get(self.base_url + "/registration/5d31a494f8829a7b37980d1d4dd1d59d")
        driver.find_element_by_id("sf_guard_user_username").send_keys("onderasd")
        driver.find_element_by_link_text("Caucasian").click()
        driver.find_element_by_id("sf_guard_user_password").send_keys("12071907")
        driver.find_element_by_id("sf_guard_user_password_again").send_keys("12071907")
        driver.find_element_by_id("sf_guard_user_first_name").send_keys("onder")
        driver.find_element_by_id("sf_guard_user_last_name").send_keys("ozturk")
        driver.find_element_by_id("sf_guard_user_zip_code").send_keys("12345345")
        driver.find_element_by_xpath("(//a[contains(text(),'02')])[2]").click()
        driver.find_element_by_link_text("01").click()
        driver.find_element_by_link_text("1933").click()
        driver.find_element_by_id("sf_guard_user_gender_m").click()
        driver.find_element_by_id("profile_terms").click()
        driver.find_element_by_id("profile_privacy").click()
        driver.find_element_by_link_text("SAVE CHANGES").click()
    
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
