from selenium import webdriver

from pages.loginpageobjects import loginPOM

driver = webdriver.Chrome()

url = "https://practicetestautomation.com/practice-test-login/"
def test_log(self):
    driver.get(url)

    self.loginPage_Obj = loginPOM(driver)

    self.loginPage_Obj.enterUserName("student")
    self.loginPage_Obj.enterPassWord("Password123")
    HomePOM_Obj = self.loginPage_Obj.clickSubmitButton()

    successText = HomePOM_Obj.getLoggedSuccessText()
    print(successText)

    driver.close()

