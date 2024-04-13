from BaseClass import BasePage
from selenium.webdriver.common.by import By

class SeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self,name_element):
        return self.find_element((By.CLASS_NAME,name_element),time=2).click()

    def check_navigation_bar(self,name_element):
        List_bars = self.find_elements((By.CSS_SELECTOR,name_element),time=2)
        Menu = [x.text for x in List_bars if len(x.text) > 0]
        return Menu
    def get_element_by_class(self,name_element):
        return self.find_element((By.CLASS_NAME,name_element),time=2)
    def get_elements_by_class(self,name_element):
        return self.find_elements((By.CLASS_NAME,name_element),time=2)
    def get_element_by_ID(self,name_element):
        return self.find_element((By.ID,name_element),time=2)
    def get_element_by_link(self,name_element):
        return self.find_element((By.XPATH,'//a[@href="' + name_element +'"]'),time=2)
    def get_elements_in_selector(self,name_element):
        return self.find_element((By.CSS_SELECTOR,name_element),time=2)
