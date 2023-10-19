import time
from random import choice

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, init_system, authenticating
from data.data import *
from locators.locators import *

# Корзина
def test_add_to_cart_from_catalog(driver, init_system): # Добавление продукта в корзину с главной страницы
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Запоминаем продукты
    item1 = driver.find_element(By.CSS_SELECTOR, ITEM_4).text
    item2 = driver.find_element(By.CSS_SELECTOR, ITEM_0).text
    # Кладем продукты в корзину
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_1).click()
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_2).click()
    # Переходим в корзину
    driver.find_element(By.XPATH, SHOPPING_CART_BUTTON).click()
    # Узнаем сколько продуктов в корзине
    number_of_products = driver.find_element(By.XPATH, NUMBER_OF_PRODUCTS_IN_CART)
    number = int(number_of_products.get_attribute('textContent'))
    # Смотрим какие продукты есть в корзине
    product1 = driver.find_element(By.CSS_SELECTOR, ITEM_4)
    product2 = driver.find_element(By.CSS_SELECTOR, ITEM_0)
    # Проверяем соответствие продуктов в корзине
    assert number == 2 # Проверка количества товаров в корзине
    assert product1.get_attribute('textContent') == item1, 'Названия продуктов не совпадают' # Проверка товара номер 1
    assert product2.get_attribute('textContent') == item2, 'Названия продуктов не совпадают' # Проверка товара номер 2

def test_remove_product_from_cart(driver, init_system): # Проверка удаления товара из корзины
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # добавляем товар в корзину
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_1).click()
    # Переходим в корзину
    driver.find_element(By.XPATH, SHOPPING_CART_BUTTON).click()
    # Удаляем товар из корзины
    driver.find_element(By.XPATH, REMOVE_FROM_CART).click()
    # Проверяем отсутствие товара в корзине
    removed_item = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ITEM_4)))
    assert removed_item == True, 'Товар не удален из корзины'

def test_add_item_in_cart_from_item_page(driver, init_system): # Проверка добавления продукта в корзину со страницы продукта
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
    # Проверяем товар в корзине
    item_in_cart = driver.find_element(By.CSS_SELECTOR, ITEM_4)
    assert item_in_cart.text == item, 'Товар не добавлен в корзину'

def test_remove_item_from_item_page(driver, init_system): # Проверка удаления продукта из корзины со страницы продукта
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Переходим на страницу товара
    driver.find_element(By.CSS_SELECTOR, ITEM_4).click()
    # Добавляем товар в корзину
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_1).click()
    # Удаляем продукт из корзины
    driver.find_element(By.XPATH, REMOVE_FROM_CART).click()
    # Переходим в корзину
    driver.find_element(By.XPATH, SHOPPING_CART_BUTTON).click()
    # Проверяем отсутствие товара в корзине
    removed_item = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ITEM_4)))
    assert removed_item == True, 'Товар не удален из корзины'

def test_click_on_item_picture(driver, init_system): # Проверка перехода на страницу товара по картинке
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Фиксируем что был за товар
    item = driver.find_element(By.CSS_SELECTOR, ITEM_4).text
    # Переходим на страницу товара по картинке
    picture_clk = driver.find_element(By.XPATH, ITEM_IMAGE)
    picture_clk.click()
    # Проверяем тот ли товар
    item_name = driver.find_element(By.XPATH, ITEM_NAME).text
    assert item_name == item

def test_click_on_item_name(driver, init_system): # Проверка перехода на страницу товара по его названию
    # Авторизация
    init_system.authenticating(LOGIN, PASSWORD, driver)
    # Запоминаем товар
    item = driver.find_element(By.CSS_SELECTOR, ITEM_4).text
    # Переходим на страницу товара
    driver.find_element(By.CSS_SELECTOR, ITEM_4).click()
    # Проверяем тот ли товар
    item_name = driver.find_element(By.XPATH, ITEM_NAME).text
    assert item_name == item, 'Товар не соответствует'


# def test_remove_item_from_the_cart_list(driver, authenticating):
#     random_items = driver.find_elements(By.CSS_SELECTOR, 'button.btn_inventory')
#     first_item = choice(random_items)
#     first_item.click()
#     second_item = choice(random_items)
#     second_item.click()
#
#     driver.get('https://www.saucedemo.com/cart.html')
#     # driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
#     list_items_before = driver.find_elements(By.CSS_SELECTOR, 'div.cart_item') #2
#     # driver.find_element(By.CSS_SELECTOR, 'button.cart_button').click()
#     driver.find_elements(By.CSS_SELECTOR, 'button.cart_button')[0].click()
#     list_items_after = driver.find_elements(By.CSS_SELECTOR, 'div.cart_item') #1
#     assert len(list_items_before) == len(list_items_after) + 1