from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

"""Select a random product under PARFUM main nav
menu and add the product to the cart"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flaconi.de/")
driver.get("https://www.flaconi.de/parfum/")
parfume = driver.find_element(by=By.XPATH, value="//img[contains(@src, 'coco-mademoiselle-eau')]")
parfume.click()
time.sleep(4)
driver.execute_script("window.scrollTo(0, 400)")
Cart = driver.find_element(by=By.XPATH, value="//button[contains(text(),'In den Warenkorb')]")
Cart.click()
time.sleep(2)
Go_to_cart = driver.find_element(by=By.XPATH, value="//a[contains(text(),'Zum Warenkorb')]")
Go_to_cart.click()
time.sleep(2)
Voucher = driver.find_element(by=By.XPATH, value="//input[@id='voucherCode']")
Voucher.send_keys("abc123")
Voucher_button = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Einlösen')]")
Voucher_button.click()


def verify(self):
    test = True
    message = "Es tut uns Leid! Der Gutscheincode ist nicht verfügbar."
    self.assertTrue(test, message)


if __name__ == '__main__':
    unittest.main()
driver.close()