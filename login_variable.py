import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_a_login_success(driver): 
        driver.find_element(By.ID, "Email").send_keys("ramita.digmi01@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("ramita12345")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
        
