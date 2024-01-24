import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class ChromeBrowser:

    def __init__(self, url: str, wait_time: int):
        self.url = url
        self.wait_time = wait_time

    def get_html_page(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(self.url)
        time.sleep(self.wait_time)
        html_page = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        return html_page
