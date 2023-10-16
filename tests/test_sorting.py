from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, init_system, authenticating, sorting
from data.data import *
from locators.locators import *

def test_Z_A_sorting(driver, sorting):
    #Выбор метода сортировки
    driver.find_element(By.XPATH, ZA_FILTER).click()
    #Проверка корректности сортировки
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, SORTED_ITEMS)))
    item_lst = []
    for item in items:
        item_lst.append(item.text)
    assert item_lst == list(reversed(sorted(item_lst))), 'Сортировка не сработала'

def test_A_Z_sorting(driver, sorting):
    # Выбор метода сортировки от A до Z
    select_a_z = driver.find_element(By.XPATH, AZ_FILTER)
    select_a_z.click()
    #Проверка корректности сортировки
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, SORTED_ITEMS)))
    item_lst = []
    for item in items:
        item_lst.append(item.text)
    assert item_lst == list(sorted(item_lst)), 'Сортировка не сработала'

def test_low_to_high_sorting(driver, sorting):
    # Выбор метода сортировки
    driver.find_element(By.XPATH, LO_HI_FILTER).click()
    prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, SORTED_BY_PRICE)))
    price_lst = []
    for price in prices:
        price_lst.append(float(price.text[1:]))
    assert price_lst == list(sorted(price_lst)), 'Сортировка не сработала'

def test_high_to_low_sorting(driver, sorting):
    # Выбор метода сортировки
    select_z_a = driver.find_element(By.XPATH, HI_LO_FILTER)
    select_z_a.click()
    # Проверка корректности сортировки
    prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, SORTED_BY_PRICE)))
    price_lst = []
    for price in prices:
        price_lst.append(float(price.text[1:]))
    assert price_lst == list(reversed(sorted(price_lst))), 'Сортировка не сработала'