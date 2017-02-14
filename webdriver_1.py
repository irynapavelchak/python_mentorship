from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:/Python27/chromedriver-Windows')
driver.get("https://jysk.ua/")

inputElement = driver.find_element_by_id("edit-query")
#inputElement = driver.find_element_by_xpath("//input[@placeholder = 'Шукати товар або категорію...']")

inputElement.send_keys("RYSLINGE")

inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("JYSK"))

    # You should see "cheese! - Google Search"
    print driver.title

    resultElement = driver.find_element_by_xpath("//div[@class = 'view-header']/h1")
    result = resultElement.text
    print result

    #assert result.find('8') != -1:

finally:
    driver.quit()

