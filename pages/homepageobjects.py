from selenium.webdriver.common.by import By


class HomePOM():

    loggedMessage = (By.XPATH,"//h1[text()='Logged In Successfully']")

    def __init__(self,driver):
        self.driver = driver

    def getLoggedSuccessText(self):
        return self.driver.find_element(*self.loggedMessage).text



