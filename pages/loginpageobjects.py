from selenium.webdriver.common.by import By

from pages.homepageobjects import HomePOM


class loginPOM():

    _username = (By.ID,"username")
    _password = (By.ID,"password")
    _submitButton = (By.ID,"submit")


    def __init__(self,driver):
        self.driver = driver


    def enterUserName(self,username):
        self.driver.find_element(*self._username).send_keys(username)
        print("Username entered successfully")

    def enterPassWord(self,password):
        self.driver.find_element(*self._password).send_keys(password)
        print("Password entered successful")

    def clickSubmitButton(self):
        self.driver.find_element(*self._submitButton).click()
        return HomePOM(self.driver)

