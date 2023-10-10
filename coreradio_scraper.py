import requests
from bs4 import BeautifulSoup
import time

def site_requests(attribute, value, total_pages=20):
    
    site_url = "https://coreradio.online/page/"
    
    id_list = []
    token_list = []
    elements_list = []

    genre = ""
    country= ""
    artist = ""
    title = ""

    try:
        response = requests.get(site_url)
        #if the response isn't correctly done, retry after 60 seconds
    except:
        time.sleep(5)
        response = requests.get(site_url)

    
    time.sleep(5)

    return response


response = site_requests("genre", "rock")
print(response)