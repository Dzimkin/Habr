from base import BasePage
from selenium.webdriver.common.by import By


class LOCATORS:
    FIELD = (By.CLASS_NAME, 'tm-input-text-decorated__input')
    BUTTON = (By.CLASS_NAME, 'tm-header-user-menu__icon_search')
    ARTICLES_LIST = (By.CLASS_NAME, 'tm-articles-list')
    HEADER = (By.CSS_SELECTOR, 'h1[class*="tm-section-name__text"]')
    TABS = (By.CSS_SELECTOR, 'a[class*="tm-main-menu__item"]')
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email_field']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password_field']")
    RECAPTCHA_CHECKBOX = (By.CLASS_NAME, "rc-anchor-center-item rc-anchor-checkbox-holder")


class HabrHelper(BasePage):

    def get_header_by_text(self, text):
        elements = self.find_elements(LOCATORS.HEADER)
        result_list = [element for element in elements if element.text.strip() == text]
        return result_list[0] if result_list else None

    def enter_word(self, word):
        search_field = self.find_element(LOCATORS.FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        button = self.find_element(LOCATORS.BUTTON)
        button.click()
        return button

    def get_tab_by_name(self, name):
        tabs = self.find_elements(LOCATORS.TABS)
        for tab in tabs:
            if tab.text.strip() == name:
                return tab

    def get_articles(self):
        articles_list = self.find_element(LOCATORS.ARTICLES_LIST)
        return articles_list.find_elements(by=By.XPATH, value=".//*")

    def find_login_button(self):
        return self.find_element(LOCATORS.LOGIN_BUTTON)
