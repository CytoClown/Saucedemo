import time
import pytest
from selenium import webdriver
from authorization import authorizationSystem
from selenium.webdriver.common.by import By
from data.data import MAIN_PAGE, LOGIN, PASSWORD
from locators.locators import *
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture
def init_system():
    system = authorizationSystem()
    yield system
    # system.return_site_to_basic_conditions(driver)

@pytest.fixture
def authenticating(driver):
    driver.get(MAIN_PAGE)
    # Авторизация
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield authenticating

@pytest.fixture
def burger_menu(driver, authenticating):
    driver.find_element(By.XPATH, BURGER_MENU).click()
    time.sleep(1)
    yield burger_menu

@pytest.fixture
def sorting(driver, authenticating):
    # Вызов выпадающего списка фильтра
    driver.find_element(By.XPATH, FILTER_LIST).click()
    yield sorting

