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
                        page_list.append(elements_list)
        
            subtoken = subtoken+1
    
    return page_list

'''
def calling(attribute, value, total_page):
    for i in range(1, total_page+1):
        elements = site_requests(attribute, value, i)
        if len(elements) != 0:
            if type(attribute) == str:    
                attribute = attribute_encoding(attribute)
            attribute_messages = {
            0: "Le releases il cui genere contiene il {} sono: ",
            1: "Le releases il cui paese è {} sono: ",
            2: "Le releases dell'artista {} sono: ",
            3: "Le releases il cui titolo è {} sono: ",
            4: "Le releases globali delle ultime {} pagine sono: "
            }

            if attribute in attribute_messages:
                message = attribute_messages[attribute]
                if attribute == 4:
                    message = message.format(total_page)
                else:
                    message = message.format(value)
                print(message)
                print(elements)


'''




def calling(string):
    command, flags, values, total_pages = arguments_checker(string)
    print("Command: ", command)
    print("Flags: ", flags)
    print("Values: ", values)
    print("Total pages: ", total_pages)



    if command == None:
        print("Error: flag not found")
        return None
    else:
        if command == "/all":
            for i in range(1, total_pages+1):
                elements = site_requests(command, flags, values, i)
                print(elements)
        elif command == "/filter":
            for i in range(1, total_pages+1):
                elements = site_requests(command, flags, values, i)
                print(elements)
        else:
            print("Error: command not found")
            return None




command = "/filter -gac prospective, italy, progressive metalcore 1"
calling(command)
