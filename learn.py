from bs4 import BeautifulSoup
import requests

samsung_a50 = 'https://www.jumia.co.ke/galaxy-a50-128gb-rom-4gb-ram-4000mah-dual-sim-4g-blue-samsung-mpg151241.html'

# def getSoup(url):
#     html = requests.get(url)
#     return BeautifulSoup(html.content, 'html.parser')

html  = requests.get(samsung_a50)
soup = BeautifulSoup(html.content, 'html.parser')

samsung_a50_Name =  soup.h1.contents[0]
Price = soup.find(attrs={"class":"-b -ltr -tal -fs24"})
samsung_a50_Price = Price.contents[0]



print(radio)