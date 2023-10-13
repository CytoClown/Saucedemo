import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome()

# Авторизация
def test_placeholder():  # Проверка плейсхолдеров
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_place = driver.find_element(By.XPATH, '//input[@placeholder="Username"]').accessible_name
    password_place = driver.find_element(By.XPATH, '//input[@placeholder="Password"]').accessible_name
    assert username_place == 'Username'
    assert password_place == 'Password'

def test_login_form(): # Проверка корректного логина и пароля
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()

def test_login_form_incorrect(): # Проверка некорректного логина и пароля
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(3)

    error_msg = driver.find_element(By.XPATH, '//h3').text

    assert driver.current_url == "https://www.saucedemo.com/"
    assert error_msg == 'Epic sadface: Username and password do not match any user in this service'
    driver.quit()

# Корзина
def test_add_to_cart_from_catalog(): # Добавление продукта в корзину с главной страницы
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item1 = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    item2 = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    add_to_cart_button1 = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button1.click()

    add_to_cart_button2 = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_button2.click()

    shopping_cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_button.click()

    number_of_products = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    number = int(number_of_products.get_attribute('textContent'))

    product1 = driver.find_element(By.CSS_SELECTOR, '.cart_list .cart_item:nth-of-type(3) .inventory_item_name') # a[id="item_4_title_link"] > div[class="inventory_item_name"]
    product2 = driver.find_element(By.CSS_SELECTOR, '.cart_list .cart_item:nth-of-type(4) .inventory_item_name')

    time.sleep(3)

    assert number == 2 # Проверка количества товаров в корзине
    assert product1.get_attribute('textContent') == item1 #'Sauce Labs Backpack' # Проверка товара номер 1
    assert product2.get_attribute('textContent') == item2 # Проверка товара номер 2
    driver.quit()
def test_remove_product_from_cart(): # Проверка удаления товара из корзины
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # добавляем товар в корзину
    add_to_cart_button1 = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button1.click()
    # Переходим в корзину
    shopping_cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_button.click()
    time.sleep(1)
    # Удаляем товар из корзины
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()
    time.sleep(1)
    # Проверяем отсутствие товара в корзине
    removed_item = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')))
    assert removed_item == True
    driver.quit()
def test_add_item_in_cart_from_item_page(): # Проверка добавления продукта в корзину со страницы продукта
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Запоминаем товар
    item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    # Переходим на страницу товара
    click_on_product = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    click_on_product.click()
    time.sleep(1)
    # Добавляем товар в корзину
    add_item_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_item_to_cart.click()
    time.sleep(1)
    # Переходим в корзину
    shopping_cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_button.click()
    time.sleep(1)
    # Проверяем товар в корзине
    item_in_cart = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    assert item_in_cart.text == item
    driver.quit()
def test_remove_item_from_item_page(): # Проверка удаления продукта из корзины со страницы продукта
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # Переходим на страницу товара
    time.sleep(1)
    click_on_product = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    click_on_product.click()
    time.sleep(1)
    # Добавляем товар в корзину
    add_item_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_item_to_cart.click()
    time.sleep(1)
    # Удаляем продукт из корзины
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()
    #Переходим в корзину
    shopping_cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_button.click()
    time.sleep(1)
    # Проверяем отсутствие товара в корзине
    removed_item = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')))
    assert removed_item == True
    driver.quit()

def test_click_on_item_picture(): # Проверка перехода на страницу товара по картинке
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # Переходим на страницу товара
    time.sleep(1)
    # Фиксируем что был за товар
    item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    # Переходим на страницу товара по картинке
    picture_clk = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]')
    picture_clk.click()
    #Проверяем тот ли товар
    item_name = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text
    assert item_name == item
    driver.quit()
def test_click_on_item_name(): # Проверка перехода на страницу товара по его названию
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Запоминаем товар
    item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    # Переходим на страницу товара
    click_on_product = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    click_on_product.click()
    time.sleep(1)
    # Проверяем тот ли товар
    item_name = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text
    assert item_name == item
    driver.quit()
# Оформление заказа
def test_order_with_correct_data(): # Оформление заказа используя корректные данные
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Запоминаем товар
    item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    # Переходим на страницу товара
    click_on_product = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    click_on_product.click()
    time.sleep(1)
    # Добавляем товар в корзину
    add_item_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_item_to_cart.click()
    time.sleep(1)
    # Переходим в корзину
    shopping_cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_button.click()
    time.sleep(1)
    # Переходим к оформлению заказа
    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()
    # Заполняем данные пользователя
    first_name_field = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name_field.send_keys("Ivan")
    time.sleep(0.5)
    last_name_field = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name_field.send_keys("Ivanov")
    time.sleep(0.5)
    postal_code_field = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    postal_code_field.send_keys("123456")
    time.sleep(0.5)
    # Нажимаем кнопку Continue
    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()
    #Запоминаем товар, который добавлен в заказ
    item_in_checkout = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text
    time.sleep(1)
    # Нажимаем кнопку Finish
    finish_button = driver.find_element(By.XPATH, '//button[@data-test="finish"]')
    finish_button.click()
    time.sleep(1)
    # Проверяем соответствие товара и успех заказа
    assert item_in_checkout == item
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    driver.quit()

def test_Z_A_sorting():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    # time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    # time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # time.sleep(1)
    #Вызов выпадающего списка фильтра
    select_list = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    select_list.click()
    #Выбор метода сортировки
    select_z_a = driver.find_element(By.XPATH, '//option[@value="za"]')
    select_z_a.click()
    #Проверка корректности сортировки
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_name"]')))
    item_lst = []
    for item in items:
        item_lst.append(item.text)
    assert item_lst == list(reversed(sorted(item_lst))), 'Сортировка не сработала'
    driver.quit()

def test_A_Z_sorting():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    #Вызов выпадающего списка фильтра
    select_list = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    select_list.click()
    #Выбор метода сортировки не установленного по умолчанию
    select_z_a = driver.find_element(By.XPATH, '//option[@value="za"]')
    select_z_a.click()
    # Выбор метода сортировки от A до Z
    select_a_z = driver.find_element(By.XPATH, '//option[@value="az"]')
    select_a_z.click()
    #Проверка корректности сортировки
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_name"]')))
    item_lst = []
    for item in items:
        item_lst.append(item.text)
    assert item_lst == list(sorted(item_lst)), 'Сортировка не сработала'
    driver.quit()


def test_low_to_high_sorting():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Вызов выпадающего списка фильтра
    select_list = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    select_list.click()
    # Выбор метода сортировки
    select_z_a = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    select_z_a.click()
    prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_price"]')))
    price_lst = []
    for price in prices:
        price_lst.append(float(price.text[1:]))

    assert price_lst == list(sorted(price_lst)), 'Сортировка не сработала'
    driver.quit()

def test_high_to_low_sorting():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Вызов выпадающего списка фильтра
    select_list = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    select_list.click()
    # Выбор метода сортировки
    select_z_a = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    select_z_a.click()
    # Проверка корректности сортировки
    prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_price"]')))
    price_lst = []
    for price in prices:
        price_lst.append(float(price.text[1:]))
    assert price_lst == list(reversed(sorted(price_lst))), 'Сортировка не сработала'
    driver.quit()

#Бургер меню
def test_logout(): # Выход из системы
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Вызов бургер меню
    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()
    time.sleep(1)
    # Нажимаем кнопку LogOut
    logout_button = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
    logout_button.click()
    time.sleep(1)
    # Проверяем что вышли
    assert driver.current_url == 'https://www.saucedemo.com/'
    driver.quit()

def test_about():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Вызов бургер меню
    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()
    time.sleep(1)
    # Нажимаем кнопку About
    about_button = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
    about_button.click()
    time.sleep(1)
    # Проверяем что куда-то перешли
    text = driver.find_element(By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-sere2z"]').text
    assert text == 'The world relies on your code. Test on thousands of different device, browser, and OS configurations–anywhere, any time.'
    driver.quit()

def test_reset_app_state():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Вводим логин
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)
    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    # Жмем кнопку логин
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    # Добавляем продукт в корзину
    add_to_cart_product = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_product.click()
    # Вызов бургер меню
    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()
    time.sleep(1)
    # Нажимаем кнопку Reset
    reset_button = driver.find_element(By.XPATH, '//a[@id="reset_sidebar_link"]')
    reset_button.click()
    time.sleep(1)
    # Переходим в карточку товара
    go_to_item_page = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    go_to_item_page.click()
    time.sleep(1)
    # Проверяем что сайт восстановился до исходного состояния
    button = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')))
    assert button == True
    driver.quit()






