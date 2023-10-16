import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, init_system, burger_menu, authenticating
from data.data import *
from locators.locators import *

#Бургер меню
def test_logout(driver, burger_menu): # Выход из системы
    # Нажимаем кнопку Logout
    driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
    # Проверяем что вышли
    assert driver.current_url == MAIN_PAGE

def test_about(driver, burger_menu):
    # Нажимаем кнопку About
    driver.find_element(By.XPATH, ABOUT_BUTTON).click()
    # Проверяем что куда-то перешли
    text = driver.find_element(By.XPATH, ABOUT_TEXT).text
    assert text == 'The world relies on your code. Test on thousands of different device, browser, and OS configurations–anywhere, any time.'

def test_reset_app_state(driver, burger_menu):
    # Добавляем продукт в корзину
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_1).click()
    # Нажимаем кнопку Reset
    driver.find_element(By.XPATH, RESET_BUTTON).click()
    # Переходим в карточку товара
    driver.find_element(By.CSS_SELECTOR, ITEM_4).click()
    # Проверяем что сайт восстановился до исходного состояния
    button = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.XPATH, REMOVE_FROM_CART)))
    assert button == True, 'Продукт не удален из корзины'