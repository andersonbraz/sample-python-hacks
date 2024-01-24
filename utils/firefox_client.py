import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup


class FirefoxBrowser:

    def __init__(self, url: str, wait_time: int):
        self.url = url
        self.wait_time = wait_time

    def get_html_page(self):

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        driver.get(self.url)
        time.sleep(self.wait_time)
        html_page = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        return html_page
