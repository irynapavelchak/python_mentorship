# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that
from time import sleep


class MainPage(object):

    def __init__(self, driver):
        self.driver = driver

    def search_action(self, search_text):
        self.search_text = search_text
        inputElement = self.driver.find_element_by_id("edit-query")
        inputElement.send_keys(search_text)
        inputElement.submit()

    def get_result(self):
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(self.driver, 10).until(EC.title_contains("JYSK"))

        print self.driver.title

        resultElement = self.driver.find_element_by_xpath("//div[@class = 'view-header']/h1")
        result = resultElement.text
        return result



    def click_first_element(self):
        self.driver.find_element_by_xpath("//*[@id='node-272253']/figure/a/img").click()



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
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_link_text("Залишити відгук").click()
        # element7.click()

class Vidguk(object):
    def __init__(self, driver):
        self.driver = driver

    def set_star(self):
        starElement = self.driver.find_element_by_xpath("//*[@id='rating-select']/div/span[1]")
        #("//dic[@class = 'stars rating-select']/span[@class = 'star-0 full']")
        starElement.click()


    def set_tema(self, tema):
        self.tema = tema
        temaElement = self.driver.find_element_by_xpath("//input[@name = 'title']")
        temaElement.click()
        temaElement.send_keys(tema)


    def set_vidguk(self, vidguk_text):
        self.vidguk_text = vidguk_text
        vidgElement = self.driver.find_element_by_id("edit-body")
        vidgElement.click()
        vidgElement.send_keys(vidguk_text)


    def set_imja(self, imja):
        self.imja = imja
        nameElement = self.driver.find_element_by_id("edit-author")
        nameElement.click()
        nameElement.send_keys(imja)


    def set_misto(self, misto):
        self.misto = misto
        mistoElement = self.driver.find_element_by_id("edit-city")
        mistoElement.click()
        mistoElement.send_keys(misto)


    def set_email(self, email):
        self.email = email
        emailElement = self.driver.find_element_by_id("edit-email")
        emailElement.click()
        emailElement.send_keys(email)


    def click_send_vidguk(self):
        self.driver.find_element_by_id("edit-submit--4").click()

    def check_validation_failed(self):
        self.failed_res = 0
        if len(self.driver.find_elements_by_xpath("//*[@id=\"jysk-reviews-add-review-form\"]/div/div/div[9]")) == 0:
            self.failed_res = 1

        assert self.failed_res == 0






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
    #mainPage.search_text = "RYSLINGE"

    mainPage.search_action("RYSLINGE")
    a = mainPage.get_result()
    assert_that('8' in a)
    mainPage.click_first_element()

    firstElement = FirstElementPage(driver)
    firstElement.check_name()
    firstElement.check_descr()
    firstElement.check_vidguks_bottom()
    firstElement.click_vidguks()
    # firstElement.check_vidguks_amount()
    firstElement.leave_vidguk()

    vidgukElement = Vidguk(driver)
    vidgukElement.set_star()
    vidgukElement.set_tema('Vidguk 1')
    vidgukElement.set_vidguk('bla bla bla')

    vidgukElement.set_imja('Iryna')
    vidgukElement.set_misto('Che')
    vidgukElement.set_email('iryna.pavelchak@gmail.com')
    vidgukElement.click_send_vidguk()
    sleep(2)
    vidgukElement.check_validation_failed()

    tear_down_driver(driver)


if __name__ == "__main__":
    test_search_ryslinge()
