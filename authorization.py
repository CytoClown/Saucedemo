import time
from selenium.webdriver.common.by import By
from data.data import MAIN_PAGE
from locators.locators import *


class authorizationSystem:
    def authenticating(self, username, password, driver):
        driver.get(MAIN_PAGE)
        # Авторизация
        driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(username)
        driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        return 'Пользователь авторизован'

    def return_site_to_basic_conditions(self, driver):
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        driver.find_element(By.XPATH, '//a[@id="reset_sidebar_link"]').click()
        return 'Сайт в исходном состоянии'
