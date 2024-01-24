import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup


class EdgeBrowser:

    def __init__(self, url: str, wait_time: int):
        self.url = url
        self.wait_time = wait_time

    def get_html_page(self):

        options = webdriver.EdgeOptions()
        options.add_argument("--headless")

        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        driver.get(self.url)
        time.sleep(self.wait_time)
        html_page = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        return str(html_page)
