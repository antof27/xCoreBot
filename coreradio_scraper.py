import requests
from bs4 import BeautifulSoup
import time



def song_cleaning(song):
    song = song.split("(")[0].strip()
    song = song.split("[")[0].strip()
    return song




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
                        genre = token.split(":")[1].strip()
                        genre = genre.split("/")

                    elif subtoken%3 == 1:
                        country = token.split(":")[1].strip()
                    
                    elif subtoken%3 == 2:
                        artist = token.split("-")[0].strip()
                        song = token.split("-")[1].strip()


                        print("artist : "   + artist)
                        print("song : " + song)

                        
                            
                    

                subtoken = subtoken+1

    #time.sleep(5)

    return id_list


a_tags = site_requests("genre", "rock")
