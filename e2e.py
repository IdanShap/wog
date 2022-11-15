from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    '''it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.'''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()), options=chrome_options)

    scores_status = False
    result = chrome_driver.find_elements_by_class_name("score")

    return scores_status


def main():
    '''The main function will return -1 as an OS exit
code if the tests failed and 0 if they passed.'''
    pass