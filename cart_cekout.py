import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import login_variable




class TestDemoWebShop(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://demowebshop.tricentis.com/"
        self.login = "https://demowebshop.tricentis.com/login"

     
    def test_a_cart_success(self): #testcasepositive
        driver = self.driver
        driver.get(self.url)
        driver.get(self.login)
        login_variable.test_a_login_success(driver)
        driver.find_element(By.XPATH, "//h2[@class='product-title']//a[contains(text(),'14.1-inch Laptop')]").click()
        driver.find_element(By.ID, "addtocart_31_EnteredQuantity").click
        driver.find_element(By.ID, "add-to-cart-button-31").click()
        driver.find_element(By.CLASS_NAME, "cart-label").click()
        titlepage = driver.title
        self.assertTrue = (titlepage == "shoping cart")
        country = driver.find_element(By.ID, "CountryId")
        negara = Select (country)
        negara.select_by_visible_text("United States")
        driver.find_element(By.ID, "ZipPostalCode").send_keys("117116")
        driver.find_element(By.NAME, "estimateshipping").click()
        driver.find_element(By.NAME, "removefromcart").click()
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        titlepage = driver.title
        self.assertTrue = (titlepage == "checkout")
        billing = driver.find_element(By.ID,"billing-address-select")
        almtbil = Select (billing)
        almtbil.select_by_visible_text("ramita ram, aa, aa, AA (Armed Forces Americas) aa, United States")
        driver.find_element(By.XPATH,"//input[@onclick='Billing.save()']").click()
        
        #disini coding mentok mba, tombol next tidak bisa di ambil element nya, bisa di ambil  sih degan path, cuma pas di run gagal
      
        
        
def tearDown(self):
    self.driver.close()
   

if __name__ == "__main__":
    unittest.main()
        
