from selenium import webdriver

from pages.loginpageobjects import loginPOM

driver = webdriver.Chrome()

url = "https://practicetestautomation.com/practice-test-login/"

driver.get(url)

loginPage_Obj = loginPOM(driver)

loginPage_Obj.enterUserName("student")
loginPage_Obj.enterPassWord("Password123")
HomePOM_Obj = loginPage_Obj.clickSubmitButton()

successText = HomePOM_Obj.getLoggedSuccessText()
print(successText)

driver.close()

