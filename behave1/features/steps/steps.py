# -*- coding: utf-8 -*-
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that
from time import sleep

@given("open '{page_url}' ")
def set_up_driver(context, page_url):
    context.driver = webdriver.Chrome('C:/Python27/chromedriver-Windows')
    context.driver.get(page_url)

@then("do search by '{search_text}' ")
def search_action(context, search_text):
    context.search_text = search_text
    inputElement = context.driver.find_element_by_id("edit-query")
    inputElement.send_keys(search_text)
    inputElement.submit()

@then("check that 8 results are returned")
def get_result(context):
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(context.driver, 10).until(EC.title_contains("JYSK"))

    resultElement = context.driver.find_element_by_xpath("//div[@class = 'view-header']/h1")
    result = resultElement.text
    assert_that('8' in result)

@then("click first element)
def click_first_element(context):
    context.driver.find_element_by_xpath("//*[@id='node-272253']/figure/a/img").click()

@then("check name of element")
def check_name(context):
    element3 = context.driver.find_element_by_xpath("//div[@class = 'product-name-sku']/h1[@itemprop = 'name']")
    result3 = element3.text.encode('utf-8')
    assert result3 == 'Стіл RYSLINGE + 4 стільці RYSLINGE'

@then("check description of element")
def check_descr(context):
    element4 = context.driver.find_element_by_xpath("//tbody/tr/td[@class = 'value']")
    result4 = element4.text.encode('utf-8')
    assert result4 == 'в комплекті з 2 додатковими "крилами"'

@then("check amount of feedbacks at the bottom")
def check_vidguks_bottom(context):
    element5 = context.driver.find_element_by_xpath("//div[@class = 'review-count']")
    result5 = element5.text.encode('utf-8')
    assert result5 == '4 відгуків'

@then("click on feedbacks tab")
def click_vidguks(context):
    element_vidguki = context.driver.find_element_by_css_selector("#content-tab-bar > li:nth-child(2) > a")
    self.driver.execute_script("return arguments[0].scrollIntoView();", element_vidguki)
    self.driver.find_element_by_css_selector("#content-tab-bar > li:nth-child(2) > a").click()

@then("click on leaving of feedback button")
def leave_vidguk(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_link_text("Залишити відгук").click()

@then("set feedback star")
def set_star(context):
    starElement = context.driver.find_element_by_xpath("//*[@id='rating-select']/div/span[1]")
    starElement.click()

@then("define '{tema}' ")
def set_tema(context, tema):
    context.tema = tema
    temaElement = context.driver.find_element_by_xpath("//input[@name = 'title']")
    temaElement.click()
    temaElement.send_keys(tema)

@then("define '{vidguk_text}'")
def set_vidguk(context, vidguk_text):
    self.vidguk_text = vidguk_text
    vidgElement = context.driver.find_element_by_id("edit-body")
    vidgElement.click()
    vidgElement.send_keys(vidguk_text)

@then("define '{imja}'")
def set_imja(context, imja):
    context.imja = imja
    nameElement = context.driver.find_element_by_id("edit-author")
    nameElement.click()
    nameElement.send_keys(imja)

@then("define '{misto}'")
def set_misto(context, misto):
    context.misto = misto
    mistoElement = context.driver.find_element_by_id("edit-city")
    mistoElement.click()
    mistoElement.send_keys(misto)

@then("define '{email}'")
def set_email(context, email):
    context.email = email
    emailElement = context.driver.find_element_by_id("edit-email")
    emailElement.click()
    emailElement.send_keys(email)

@then("click on sending feedback button")
def click_send_vidguk(context):
    context.driver.find_element_by_id("edit-submit--4").click()
    sleep(2)

@then("check if validation failed")
def check_validation_failed(context):
    context.failed_res = 0
    if len(context.driver.find_elements_by_xpath("//*[@id=\"jysk-reviews-add-review-form\"]/div/div/div[9]")) == 0:
        context.failed_res = 1
    assert context.failed_res == 0

@then(close browser)
def tear_down_driver(context):
    context.driver.quit()










