from bs4 import BeautifulSoup
import requests

redmi = "https://www.jumia.co.ke/redmi-note-7-pro-6.30-inch-fhd6128gb-4000mah-smartphone-black-26898382.html"


def getSoup(url):
    html = requests.get(url)
    return BeautifulSoup(html.content, 'html.parser')

soup = getSoup(redmi)
name = soup.find("h1").string
#the first radio button
radio = soup.find("input", attrs={"id":"imgs-sld-1"})
link = radio.find_next_sibling("a")
image = link.find("img")

print(image.get("data-src"))

