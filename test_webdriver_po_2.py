# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that


class MainPage(object):
    search_text = ""

    def __init__(self, driver):
        self.driver = driver

    def search_action(self):
        inputElement = driver.find_element_by_id("edit-query")
        inputElement.send_keys(self.search_text)
        inputElement.submit()

    def check_result(self):
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains("JYSK"))

        print driver.title

        resultElement = driver.find_element_by_xpath("//div[@class = 'view-header']/h1")
        result = resultElement.text
        print result
        assert_that('8' in result)

    def click_first_element(self):

        element2 = driver.find_element_by_xpath("//a[@data-raptorrecommendation='productId:S368047']/span")
        element2.submit()


class FirstElementPage(object):

    def __init__(self, driver):
        self.driver = driver

    def check_name(self):

        element3 = driver.find_element_by_xpath("//div[@class = 'product-name-sku']/h1[@itemprop = 'name']")
        result3 = element3.text
        assert result3 == 'Стіл RYSLINGE + 4 стільці RYSLINGE'

    def check_descr(self):

        element4 = driver.find_element_by_xpath("//tbody/tr/td[@class = 'value']")
        result4 = element4.text
        assert result4 == 'в комплекті з 2 додатковими "крилами"'

    def check_vidguks_bottom(self):

        element5 = driver.find_element_by_xpath("//div[@class = 'review-count']")
        result5 = element5.text
        assert result5 == '4 відгуків'


    def click_vidguks(self):

        element_vidguki = driver.find_element_by_xpath("//li/a[@class = 'tab-rating']")
        element_vidguki.submit()

    def check_vidguks_amount(self):

        element6 = driver.find_element_by_xpath("//div[@class = 'product-review-total']/div/div/div[@class = 'product-score']")
        result6 = element6.text
        assert_that('4' in result6)

    def leave_vidguk(self):

        element7 = driver.find_element_by_xpath("//a[@title = 'Залишити відгук']")
        element7.submit()



def set_up_driver():
    driver = webdriver.Chrome('C:/Python27/chromedriver-Windows')
    driver.get("https://jysk.ua/")
    return driver


def tear_down_driver(driver):
    driver.quit()


def test_search_ryslinge():
    driver = set_up_driver()

    mainPage = MainPage(driver)

    # Sets the text of search textbox
    mainPage.search_text = "RYSLINGE"

    mainPage.search_action()
    mainPage.check_result()
    mainPage.click_first_element()

    firstElement = FirstElementPage(driver)
    firstElement.check_name()
    firstElement.check_descr()
    firstElement.check_vidguks_bottom()
    firstElement.click_vidguks()
    firstElement.check_vidguks_amount()
    firstElement.leave_vidguk()



    tear_down_driver(driver)



if __name__ == "__main__":
    test_search_ryslinge()

