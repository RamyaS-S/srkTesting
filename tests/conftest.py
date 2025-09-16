from selenium import webdriver
import pytest

@pytest.fixture()
def driver_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.close()

    driver.quit()