# from Day11Assignment.pages.welcomePage import WelcomePageObjects
# from pages.welcomePage import WelcomePageObjects
from pages.welcomePage import WelcomePageObjects



def test_register(driver_fixture):
    print("something")
    driver_fixture.get("https://tutorialsninja.com/demo/")

    welcomeVariableObj = WelcomePageObjects(driver_fixture)

    welcomeVariableObj.clickMyAccountLink()
    welcomeVariableObj.clickRegisterOption()
    

# test_register()
