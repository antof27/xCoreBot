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





def site_requests(command, flags, values, page_number):

    





    site_url = "https://coreradio.online/page/" + str(page_number) 
    
    page_list = []
    elements_list = []
    

    genre = []
    country= ""
    artist = ""
    title = ""

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




command = "/filter -ac prospective, italy 1"
calling(command)
