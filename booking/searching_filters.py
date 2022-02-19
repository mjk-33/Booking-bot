from selenium.webdriver.remote.webdriver import WebDriver

class SearchingFilters:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_rating(self):
        star_rating_box = self.driver.find_element_by_id("searchboxInc")
        star_child_elements = star_rating_box.find_elements_by_css_selector('*')
        print(len(star_child_elements))

