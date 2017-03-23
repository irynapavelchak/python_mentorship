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
        inputElement = self.driver.find_element_by_id("edit-query")
        inputElement.send_keys(self.search_text)
        inputElement.submit()

    def check_result(self):
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(self.driver, 10).until(EC.title_contains("JYSK"))

        print self.driver.title

        resultElement = self.driver.find_element_by_xpath("//div[@class = 'view-header']/h1")
        result = resultElement.text
        print result
        assert_that('8' in result)

    def click_first_element(self):
        self.driver.find_element_by_xpath("//img[contains(@src, '50831')]/parent::a").click()


class FirstElementPage(object):
    def __init__(self, driver):
        self.driver = driver

    def check_name(self):
        element3 = self.driver.find_element_by_xpath("//div[@class = 'product-name-sku']/h1[@itemprop = 'name']")
        result3 = element3.text.encode('utf-8')
        print result3
        assert result3 == 'Стіл RYSLINGE + 4 стільці RYSLINGE'

    def check_descr(self):
        element4 = self.driver.find_element_by_xpath("//tbody/tr/td[@class = 'value']")
        result4 = element4.text.encode('utf-8')
        assert result4 == 'в комплекті з 2 додатковими "крилами"'

    def check_vidguks_bottom(self):
        element5 = self.driver.find_element_by_xpath("//div[@class = 'review-count']")
        result5 = element5.text.encode('utf-8')
        assert result5 == '4 відгуків'

    def click_vidguks(self):
        element_vidguki = self.driver.find_element_by_css_selector("#content-tab-bar > li:nth-child(2) > a")
        self.driver.execute_script("return arguments[0].scrollIntoView();", element_vidguki)
        self.driver.find_element_by_css_selector("#content-tab-bar > li:nth-child(2) > a").click()

    def check_vidguks_amount(self):
        element6 = self.driver.find_element_by_xpath("//div[@data-id = 'S368047']/parent::div")
        # ("//div[@class = 'stars']/div[@class = 'product-score']")
        result6 = element6.text.encode('utf-8')
        print "res6 =" + result6
        # self.assertTrue("4" in result6)
        # assert_that('4' in result6)

    def leave_vidguk(self):
        wait = WebDriverWait(driver, 10)

        self.driver.find_element_by_css_selector("#product-ratings > div > div > div > div > div > a").click()
        # element7.click()


def set_up_driver(page_url):
    driver = webdriver.Chrome('C:/Python27/chromedriver-Windows')
    driver.get(page_url)
    return driver


def tear_down_driver(driver):
    driver.quit()


def test_search_ryslinge():
    driver = set_up_driver("https://jysk.ua/")

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
    # firstElement.check_vidguks_amount()
    firstElement.leave_vidguk()

    tear_down_driver(driver)


#if __name__ == "__main__":
#    test_search_ryslinge()
