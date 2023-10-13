import requests
from bs4 import BeautifulSoup
import time
from token_extractor import arguments_checker


def song_cleaning(song):
    song = song.split("(")[0].strip()
    song = song.split("[")[0].strip()
    return song

'''
def attribute_encoding(flag):
    print(attribute)
    attribute = lower_case(attribute)
    
    attribute_mapping = {
        "genre": 0,
        "country": 1,
        "artist": 2,
        "title": 3,
        "all" : 4
    }
    
    return attribute_mapping.get(attribute, "Attribute not found")
'''

def lower_case(string):
    return string.lower()


def requests_and_soup(url):
    try:
        response = requests.get(url)
        
        #if the response isn't correctly done, retry after 60 seconds
    except:
        time.sleep(5)
        response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def values_extractor(flags, values):
    if flags is not None:
        flag_mapping = {
            "genre": None,
            "country": None,
            "artist": None,
            "title": None
        }
        
        for flag in flag_mapping:
            if flag in flags:
                index = flags.index(flag)
                flag_mapping[flag] = values[index]

        query_genre = flag_mapping["genre"]
        query_country = flag_mapping["country"]
        query_artist = flag_mapping["artist"]
        query_title = flag_mapping["title"]
    
    else:
        return None, None, None, None
    
    return query_genre, query_country, query_artist, query_title
    


def site_requests(command, flags, values, page_number):
    
    #search the genre inside the flags list and assign to the variable genre, the related index in values list
    
    
    query_genre, query_country, query_artist, query_title = values_extractor(flags, values)
    


    site_url = "https://coreradio.online/page/" + str(page_number) 
    
    
    page_list = []
    elements_list = []
    
    release_genre = []
    release_country= None
    release_artist = None
    release_title = None

    soup = requests_and_soup(site_url)
    
    #find the content div
    content_div = soup.find("div", {"id": "dle-content"})
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
                    release_genre = token.split(":")[1].strip()
                    release_genre = release_genre.split("/")
                except:
                    continue

            elif subtoken%3 == 1:
                try: 
                    release_country = token.split(":")[1].strip()
                except:
                    continue
            
            elif subtoken%3 == 2:
                try:
                    release_artist = token.split("-")[0].strip()
                    release_title = song_cleaning(token.split("-")[1].strip())

                except:
                    continue
            else:
                
                continue           
            
        
            if subtoken%3 == 2:
                elements_list = [release_genre, release_country, release_artist, release_title]

                if release_genre != None and release_country != None and release_artist != None and release_title != None:
                    if command == "/all":
                        page_list.append(elements_list)
                    elif command == "/filter":
                        #check if the release values are equal to the query values
                        if query_genre != None:
                            if not any(lower_case(query_genre) in lower_case(item) for item in release_genre):
                                continue
                        if query_country != None:
                            if lower_case(query_country) != lower_case(release_country):
                                continue
                        if query_artist != None:
                            if lower_case(query_artist) != lower_case(release_artist):
                                continue
                        if query_title != None:
                            if lower_case(query_title) != lower_case(release_title):
                                continue

                        page_list.append(elements_list)
                        
        
            subtoken = subtoken+1
    
    return page_list



def calling(string):
    command, flags, values, total_pages = arguments_checker(string)
    print("Command: ", command)
    print("Flags: ", flags)
    print("Values: ", values)
    print("Total pages: ", total_pages)



    if command == None:
        print("Error: Command not found")
        return None
    else:
        if command == "/all":
            for i in range(1, total_pages+1):
                elements = site_requests(command, flags, values, i)
                print(elements)
        elif command == "/filter":
            for i in range(1, total_pages+1):
                elements = site_requests(command, flags, values, i)
                if len(elements) == 0:
                    continue
                print(elements)
        else:
            print("Error: command not found")
            return None




command = "/all 2"
calling(command)
