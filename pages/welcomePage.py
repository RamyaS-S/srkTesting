from selenium.webdriver.common.by import By


class WelcomePageObjects():

    myAccountButtonElement = (By.XPATH, "//span[text()='My Account']")
    registerButtonOptionsElement = (By.CSS_SELECTOR,"ul[class='dropdown-menu dropdown-menu-right'] li")
    loginButtonOptionsElement = (By.CSS_SELECTOR,"ul[class='dropdown-me nu dropdown-menu-right'] li")
    registerButtonDirectElement = (By.XPATH,"//a[text()='Register']")

    def __init__(self,driver):
        self.driver = driver

    def clickMyAccountLink(self):
        self.driver.find_element(*self.myAccountButtonElement).click()
        print("My account link is clicked")

    def clickRegisterOption(self):
        self.driver.find_element(*self.registerButtonDirectElement).click()
        print("Register link is clicked")
