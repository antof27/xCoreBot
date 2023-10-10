import requests
from bs4 import BeautifulSoup
import time



def song_cleaning(song):
    song = song.split("(")[0].strip()
    song = song.split("[")[0].strip()
    return song

def attribute_encoding(attribute):
    if attribute == "genre":
        attribute = 0
    elif attribute == "country":
        attribute = 1
    elif attribute == "artist":
        attribute = 2
    elif attribute == "title":
        attribute = 3
    else:
        print("Attribute not found")
        return None
    return attribute



def site_requests(attribute, value, page_number):
    
    attribute = attribute_encoding(attribute)

    site_url = "https://coreradio.online/page/" + str(page_number) 
    
    id_list = []
    page_list = []
    elements_list = []
    
    genre = []

    country= ""
    artist = ""
    title = ""

    try:
        response = requests.get(site_url)
        
        #if the response isn't correctly done, retry after 60 seconds
    except:
        time.sleep(5)
        response = requests.get(site_url)

    soup = BeautifulSoup(response.text, "html.parser")
    
    #find the content div
    content_div = soup.find("div", {"id": "dle-content"})
    
    #find the a tags in the content div
    a_tags = content_div.find_all('a')

    for a in a_tags:
        
        if "https://coreradio.online/" in a['href'] and "https://coreradio.online/page/" not in a['href'] and a['href'][-1] != "/":

            id = a['href'].split("/")[4]
            id = id.split("-")[0]
            id = int(id)
            
            if id is None or id in id_list:
                continue
            else:
                id_list.append(id)

    information = content_div.text.strip()

    lines = information.splitlines()
    lines = [line for line in lines if line.strip() != ""]
    
    subtoken = 0
    for token in lines:
        
        if token == "more" or token == "MAIN" or token == '«' or token == '»' or token == "Load more" or "Quality:" in token or len(token) <2:
            continue
        
        else:
            if subtoken%3 == 0:
                try:
                    genre = token.split(":")[1].strip()
                    genre = genre.split("/")
                except:
                    continue

            elif subtoken%3 == 1:
                try: 
                    country = token.split(":")[1].strip()
                except:
                    continue
            
            elif subtoken%3 == 2:
                try:
                    artist = token.split("-")[0].strip()
                    title = song_cleaning(token.split("-")[1].strip())

                except:
                    continue
            else:
                continue           

        
            if subtoken%3 == 2:
                elements_list = [genre, country, artist, title]

                if genre != "" and country != "" and artist != "" and title != "":
                    if elements_list[attribute] == value or (attribute == 0 and any(value in item for item in elements_list[attribute])):
                        page_list.append(elements_list)
        
            subtoken = subtoken+1
        


    return page_list


def calling(attribute, value, total_page):
    for i in range(1, total_page+1):
        elements = site_requests(attribute, value, i)
        print("page_list: ", elements)


calling(attribute ="artist", value="Windvent", total_page=1)