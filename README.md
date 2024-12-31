Validate search functionality on the Selenium Playground website.

Approach
1. Launches the browser using Chrome WebDriver with automatic management of the driver via webdriver_manager.
2. Navigates to the Selenium Playground Table Search Demo.
3. The test interacts with the search box on the webpage, entering the search term "New York".
4. Waits for the results: Uses WebDriverWait to wait for the table rows to load after the search.
5. The number of filtered rows is checked, and it is asserted that exactly 5 rows should be displayed after searching for "New York".
The text displaying the search result summary (e.g., "Showing 1 to 5 of 5 entries") is also validated against the expected result.
6. Cleans up: Quits the browser after the test completes.


How to Run the Script
Prerequisites:
1. Python - You  should have Python installed on your local machine
2. Selenium - The test uses Selenium WebDriver to control the browser. Selenium should be installed in your Python environment. (Used selenium 4)
3. pytest - pytest is a testing framework for structuring or managing the testcases.
4. WebDriver Manager - Used webdriver_manager to automatically manage the correct version of ChromeDriver, so you do not need to worry about installing ChromeDriver manually.


Setting Up the Testing environment
1. Python installed (Mandatory)
2. Install seleenium (pip install selenium)
3. Install pytest (pip install -U pytest)
4. Install webdriver-manager (pip install webdriver-manager)

Run the Test
1. Terminal/shell - cd to python file (pytest qa_selenium_test.py)
2. In pycharm's IDE terminal (pytest) or (pytest -v)
