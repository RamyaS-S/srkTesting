from selenium.webdriver.common.by import By
class RegistrationPageObjects():

    firstnameElement = (By.ID,"input-firstname")
    lastnameElement = (By.ID,"input-lastname")
    emailElement = (By.ID, "input-email")
    telephoneElement = (By.ID,"input-telephone")
    passwordElement = (By.ID, "input-password")
    passwordConfirmElement = (By.ID, "input-confirm")
    privacyPolicyElement = (By.XPATH,"//input[@type='checkbox']")
    continueButtonElement = (By.XPATH,"//input[@type='submit']")

