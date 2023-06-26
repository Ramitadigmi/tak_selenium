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


   
    def test_a_login_success(self): #testcase1positive
        driver = self.driver
        driver.get(self.url)
        driver.get(self.login)
        login_variable.test_a_login_success(driver)
        
      
    
    def test_b_login_failed(self): #testcase1negative with wrong email and password
        driver = self.driver
        driver.get(self.url)
        driver.get(self.login)
        driver.find_element(By.ID, "Email").send_keys("ramita.di@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("ramita12")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        message = "Login was unsuccessful. Please correct the errors and try again."
        self.assertIn(message, error_message)



def tearDown(self):
    self.driver.close()
   

if __name__ == "__main__":
    unittest.main()