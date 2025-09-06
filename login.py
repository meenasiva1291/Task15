from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class orange_login():
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.loginbutton_locator = (By.XPATH, "//button[@type='submit']")
        self.dashboard_locator =(By.XPATH,"//h6[text()='Dashboard']")
        self.wait = WebDriverWait(driver, 10)

    def login(self,username,password):
        username_field = self.wait.until(expected_conditions.presence_of_element_located(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait.until(expected_conditions.presence_of_element_located(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)
        login_click = self.wait.until(expected_conditions.presence_of_element_located(self.loginbutton_locator))
        login_click.click()

    def is_login_success(self):
        # Example: check if error message present
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.dashboard_locator))
            return True
        except:
            return False
