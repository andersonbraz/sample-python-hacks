from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get('https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html')

myLink = driver.find_element(By.ID, 'cookie-btn')
time.sleep(2)
myLink.click()

time.sleep(30)
driver.quit()

