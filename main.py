import pprint 
from Scraper import Scraper

import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


pprint.pp('WELCOME TO RETAIL PRICES')

model_name = input('Enter Phone Model.. ')

Scraper(model_name)

#ask for the name of device