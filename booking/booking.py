from http import cookies
from lib2to3.pgen2 import driver
from random import choice
from select import select
from tracemalloc import start
import booking.constans as const
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from booking.searching_filters import SearchingFilters

class Booking(webdriver.Safari):
    def __init__(self, teardown = False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()
 
    def land_first_page(self):
        self.get(const.page_url)
        time.sleep(1)
    
    def __exit__(self, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def preferences_bar(self):
        try:
            cookies_button = self.find_element_by_id("onetrust-accept-btn-handler")
            cookies_button.click()
            time.sleep(1)
        except:
            return
    
    def change_language(self, language=None):
        language_element = self.find_element_by_css_selector(
            'button[data-modal-id="language-selection"]'
        )
        language_element.click()

        selected_language_element = self.find_element_by_css_selector(
            f'a[data-lang="{language}"]'
        )
        selected_language_element.click()
        time.sleep(1)

        

    def change_currency(self, currency = None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
        time.sleep(1)

    def select_destination(self, destination):
        search_bar = self.find_element_by_id('ss')
        search_bar.clear() #cleaning search bar 
        search_bar.send_keys(destination)

        choice = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        choice.click()
        time.sleep(1)
   
    def select_date(self, check_in, check_out):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()
        time.sleep(1)
    
    def guests_value(self, adults, children, rooms, children_age = []):
        guests_element = self.find_element_by_id('xp__guests__toggle')
        guests_element.click()

        #set adults value to 1 to operate easier
        decrease_adults = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        for i in range(1):
            decrease_adults.click()
            time.sleep(2)

        # add value of adults you want 
        add_adults = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(1, adults):
            add_adults.click()

        # add value of adults you want 
        add_childen = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Children"]'
        )
        for i in range(0,children):
            add_childen.click()
        
        # this if-statement checks whether children value is equal to children age array length
        # to set particual values of age 
        if(children == len(children_age)):
            for iteration, i in enumerate(children_age):
                select_age_needed = Select(self.find_element_by_css_selector(
                    f'select[data-group-child-age="{iteration}"]'
                ))
                select_age_needed.select_by_value(str(i))
        else:
            print('Error')

        # add room quantity
        add_room = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )
        for i in range(1, rooms):
            add_room.click()
        
        time.sleep(1)
    
    def search_button(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()
    
    def search_result_filters(self):

        filters = SearchingFilters(driver = self)

        filters.star_rating()

        




       



        
        
        





    
