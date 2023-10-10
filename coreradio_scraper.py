import requests
from bs4 import BeautifulSoup
import time

def site_requests(attribute, value, total_pages=20):
    
    url = "https://coreradio.online/page/"
    try:
        response = requests.get(url)
        #if the response isn't correctly done, retry after 60 seconds
    except:
        time.sleep(5)
        response = requests.get(url)

