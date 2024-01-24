from lxml import html
import requests

search_url = "https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html"
search_page = requests.get(search_url)
search_html = html.fromstring(search_page.text)
firstEntry_link = search_html.xpath('//*[@id="Industria_da_Construcao_anchor"]/')

print(search_html)