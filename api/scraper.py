import requests
from bs4 import BeautifulSoup

def get_riesgo_pais():
    url = "https://www.ambito.com/contenidos/riesgo-pais.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Busca el número de riesgo país (suele estar en un span con clase 'dato')
    dato = soup.find("div", {"class": "value"}).text.strip()
    return float(dato.replace(".", "").replace(",", "."))
