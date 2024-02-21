import pytest
import time
from pages import HabrHelper
from pages import LOCATORS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(scope='module')
def habr_helper(browser):
    return HabrHelper(browser)


def check_tab(habr_helper, tab_name):
    tab = habr_helper.get_tab_by_name(tab_name)
    tab.click()
    time.sleep(1)
    header = habr_helper.get_header_by_text(tab_name)
    assert header is not None
    assert header.text == tab_name


@pytest.mark.parametrize("tab_name", ['Все потоки', 'Разработка', 'Администрирование', 'Дизайн', 'Менеджмент',
                                      'Маркетинг', 'Научпоп'])
def test_tabs(habr_helper, tab_name):
    check_tab(habr_helper, tab_name)


def test_habr_search(habr_helper):
    habr_helper.click_on_the_search_button()
    search_field = habr_helper.enter_word('Python')
    habr_helper.press_enter(search_field)
    assert habr_helper.get_articles()


def test_login_button_presence(habr_helper):
    login_button = habr_helper.find_login_button()
    assert login_button is not None, "Кнопка 'Войти' не найдена на странице"


def test_login(habr_helper):
    login_button = habr_helper.find_element(LOCATORS.LOGIN_BUTTON)
    login_button.click()
    email_field = habr_helper.find_element(LOCATORS.EMAIL_FIELD)
    email_field.send_keys('guzich_d@tut.by')
    password_field = habr_helper.find_element(LOCATORS.PASSWORD_FIELD)
    password_field.send_keys('guzich_d@tut.by')
    recaptcha_checkbox = habr_helper.find_element(LOCATORS.RECAPTCHA_CHECKBOX)
    recaptcha_checkbox.click()
    login_button = habr_helper.find_element(LOCATORS.LOGIN_BUTTON)
    login_button.click()
    profile_image = WebDriverWait(habr_helper.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='https://assets.habr.com/habr-web/img/avatars/151.png']"))
    )
    assert profile_image is not None
