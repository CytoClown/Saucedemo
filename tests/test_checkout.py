from selenium.webdriver.common.by import By
from conftest import driver, init_system
from data.data import *
from locators.locators import *

# Оформление заказа
def test_order_with_correct_data(driver, init_system): # Оформление заказа используя корректные данные
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Запоминаем товар
    item = driver.find_element(By.CSS_SELECTOR, ITEM_4).text
    # Переходим на страницу товара
    driver.find_element(By.CSS_SELECTOR, ITEM_4).click()
    # Добавляем товар в корзину
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_1).click()
    # Переходим в корзину
    driver.find_element(By.XPATH, SHOPPING_CART_BUTTON).click()
    # Переходим к оформлению заказа
    driver.find_element(By.XPATH, CHECKOUT_BUTTON).click()
    # Заполняем данные пользователя
    driver.find_element(By.XPATH, USER_NAME).send_keys(FIRST_NAME)
    driver.find_element(By.XPATH, USER_LAST_NAME).send_keys(LAST_NAME)
    driver.find_element(By.XPATH, POSTAL_CODE).send_keys(POSTAL_CODE)
    # Нажимаем кнопку Continue
    driver.find_element(By.XPATH, CONTINUE_BUTTON).click()
    # Запоминаем товар, который добавлен в заказ
    item_in_checkout = driver.find_element(By.XPATH, ITEM_NAME).text
    # Нажимаем кнопку Finish
    driver.find_element(By.XPATH, FINISH_BUTTON).click()
    # Проверяем соответствие товара и успех заказа
    assert item_in_checkout == item, 'Продукт в корзине не соответствует выбранному'
    assert driver.current_url == CHECKOUT_URL, 'Url не соответствует'









