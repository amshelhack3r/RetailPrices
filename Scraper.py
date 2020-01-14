from bs4 import BeautifulSoup
import requests
from phoneinfo import PhoneInfo


class Scraper():
    base_uri = "https://jumia.co.ke/"
    
    def __init__(self, value):
        value = value.split()
        self.model = value[0]
        value.pop(0)
        
        # means only one value was passed to the query eg "huawei"
        if len(value) == 0:
            self.base_uri += self.model
            pass
        # means that more than 1 values were passed to the query eg "huawei y9" or "huawei y9 4gb 64gb"
        else:
            self.base_uri = Scraper.urlBuilder(self.model, *value)
            pass

        print(self.base_uri)
        self.buildList()


    def buildList(self):
        soup = Scraper.getSoup(self.base_uri)
        products = soup.find("section", attrs={"class":"products"})
        gallery = products.find_all("a", limit=10)
        
        for elem in gallery:
            link = elem.get("href")
            image = elem.find("img").get("data-src")
            name = elem.find("span", attrs={"class": "name"}).string
            price_div = elem.find("span", attrs={"class":"price"})
            price = price_div.find("span", attrs={"dir":"ltr"}).string

            print('*********************EOL***********************')
            print(name)
            print(price)
            print(image)
            print(link)
            print('*********************EOL***********************')

    @classmethod        
    def getSoup(cls, url):
        html = requests.get(url)
        return BeautifulSoup(html.content, 'html.parser')
        

    @classmethod
    def urlBuilder(cls, model, *args):
        query_string = ""
        for word in args:
            query_string += f'{word}+'
        pass

        return f'{Scraper.base_uri}{model}/?q={query_string}'
