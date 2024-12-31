# Importing necessary libraries
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Defining a pytest fixture to launch the browser before each test
@pytest.fixture()
def launch_browser():

    # Initializing the Chrome WebDriver using WebDriver Manager to handle driver installation
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigating to the target webpage for the test
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    # Maximizing the browser window for better visibility
    driver.maximize_window()

    # Yielding the WebDriver instance to the test function
    yield driver

    # After the test completes, quitting the WebDriver (closing the browser)
    driver.quit()

# Test function to verify search functionality for "New York" in the table
def test_search_new_york(launch_browser):

    # Accessing the search box element by its XPath and sending the text "New York" for the search
    searchBox = driver.find_element(By.XPATH,"//*[@id='example_filter']/label/input")
    searchBox.send_keys("New York")

    # Adding a small implicit wait to allow for the page to process the search query
    driver.implicitly_wait(2)

    # Finding all the table rows in the filtered results after the search
    rows = driver.find_elements(By.XPATH,"//*[@id='example']/tbody//tr")

    # Calculating the number of rows that are displayed after the search
    number_of_rows = len(rows)

    # Asserting that the number of rows shown should be 5 (as expected for the "New York" search)
    assert number_of_rows == 5

    # Finding the element that displays the search result info and extracting its text
    search_result_txt = driver.find_element(By.ID, "example_info").text

    # Defining the expected search result text
    expected_result = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

    # Asserting that the search result text matches the expected result
    assert search_result_txt == expected_result

