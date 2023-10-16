from selenium.webdriver.common.by import By
from conftest import driver, init_system
from data.data import *
from locators.locators import *

# Авторизация
def test_placeholder(driver):  # Проверка плейсхолдеров
    driver.get(MAIN_PAGE)
    username_place = driver.find_element(By.XPATH, USERNAME_PLACEHOLDER).accessible_name
    password_place = driver.find_element(By.XPATH, PASSWORD_PLACEHOLDER).accessible_name
    assert username_place == 'Username'
    assert password_place == 'Password'

def test_login_form(driver, init_system): # Проверка корректного логина и пароля
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Проверка перехода на страницу с товарами
    assert driver.current_url == INVENTORY_PAGE, 'Авторизоваться не удалось'

def test_login_form_incorrect(driver, init_system): # Проверка некорректного логина и пароля
    # Авторизация
    init_system.authenticating(INCORRECT_LOGIN, INCRRECT_PASSWORD, driver)
    # Получение текста сообщения об ошибке
    error_msg = driver.find_element(By.XPATH, ERROR_MSG).text
    # Проверка корректности сообщения об ошибке
    assert driver.current_url == MAIN_PAGE, 'Неверный URL'
    assert error_msg == 'Epic sadface: Username and password do not match any user in this service', 'Сообщение об ошибке не появилось, или не соответствует'








