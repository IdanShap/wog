from sys import exit
from selenium import webdriver, common
from selenium.webdriver.chrome.service import Service as chrome_service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    '''This function uses the Selenium driver for Chrome to test the Flask website and make sure it displays a score'''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions") # disable extensions to avoid interference
    chrome_options.add_argument("--headless") # running headless without opening browser window
    chrome_driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()), options=chrome_options)

    # tries to reach the website, and handling the exception if it is not reachable
    try:
        chrome_driver.get(app_url)
    except common.exceptions.WebDriverException:
        print("Error: Could not reach the website")
        return False

    result = chrome_driver.find_element(By.CLASS_NAME, "score").text
    if int(result) >= 1 or int(result) <= 1000:
        return True
    else:
        return False


def main(app_url):
    if test_scores_service(app_url):
        exit(0)
    else:
        exit("Test failed")

