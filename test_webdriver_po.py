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

def set_up_driver():
	driver = webdriver.Chrome('C:/Python27/chromedriver-Windows')
	driver.get("https://jysk.ua/")
	return driver

def tear_down_driver(driver):
	driver.quit()

def Test_search_ryslinge():
	driver = set_up_driver()

	mainPage = MainPage(driver)

	# Sets the text of search textbox
	mainPage.search_text = "RYSLINGE"

	mainPage.search_action
	mainPage.check_result

	tear_down_driver(driver)

if __name__ == "__main__":
	Test_search_ryslinge()