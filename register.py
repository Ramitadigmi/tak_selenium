import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import login_variable



class TestDemoWebShop(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://demowebshop.tricentis.com/"
        self.login = "https://demowebshop.tricentis.com/login"
        self.register = "https://demowebshop.tricentis.com/register"




    def test_a_register_success(self): #testcase2positive
        driver = self.driver
        driver.get(self.url)
        driver.get(self.register)
        login_variable.test_a_login_success(driver)
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("ramita")
        driver.find_element(By.ID, "LastName").send_keys("ram")
        driver.find_element(By.ID, "Email").send_keys("ramita.digmi01@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("ramita123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("ramita123")
        driver.find_element(By.ID, "register-button").click()

    

    def test_b_register_failed(self): #testcase2negative  with not input email
        driver = self.driver
        driver.get(self.url)
        driver.get(self.register)
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("ramita")
        driver.find_element(By.ID, "LastName").send_keys("ram")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("ramita123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("ramita123")
        driver.find_element(By.ID, "register-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        message = "Email is required."
        self.assertIn(message, error_message)



def tearDown(self):
    self.driver.close()
   

if __name__ == "__main__":
    unittest.main()