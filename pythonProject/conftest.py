import pytest
from selenium import webdriver as WD

@pytest.fixture(scope="session")
def main_open():
    driver = WD.Chrome()
    yield driver
    driver.quit()

#@pytest.fixture(scope="session")
#def login():
#    driver = WD.Chrome()
#    yield driver
#    driver.quit()

