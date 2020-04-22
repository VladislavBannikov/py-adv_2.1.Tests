from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://passport.yandex.ru/auth/'
LOGIN = 'test_login'


def _get_field(driver, _id):
    try:
        field = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, _id)))
        return field
    except TimeoutException:
        return


def get_element(driver, _css_selector): # дублирует логику _get_button
    try:
        dom_elem = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _css_selector)))
        return dom_elem
    except TimeoutException:
        return


def _get_button(driver, _css_selector): # можно было бы добавить проверку, что элемент действительно кнопка
    try:
        button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _css_selector)))
        return button
    except TimeoutException:
        return


def _text_to_field(field, text):
    try:
        field.send_keys(text)
        return field
    except Exception:
        return


def get_field_text(field):
    return field.text()


def get_password_field(driver):
    return _get_field(driver, 'passp-field-passwd')


def get_login_field(driver):
    return _get_field(driver, 'passp-field-login')


def get_enter_button(driver):
    return _get_button(driver, '.button2_type_submit')


def get_qrcode_button(driver):
    return _get_button(driver, 'passp-sign-in-button__magic-link')


def fill_login_field(field):
    return _text_to_field(field, LOGIN)

