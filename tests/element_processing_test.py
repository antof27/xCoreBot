from src.element_processing import process_elements_list


def test_process_elements_list_all_command() -> None:
    # Test with /all command
    command = "/all"
    elements_list = ["metalcore", "sweden", "imminence", "continuum"]
    release_genre = ["metalcore", "alternative rock"]
    release_country = "sweden"
    release_artist = "imminence"
    release_title = "continuum"
    songs_counter = 0
    total_songs = 5
    page_list = []
    query_genre = ""    
    query_country = ""
    query_artist = ""
    query_title = ""

    updated_songs_counter, page_list = process_elements_list(command, elements_list, query_genre, release_genre,
                            query_country, release_country, query_artist,
                            release_artist, query_title, release_title,
                            songs_counter, total_songs, page_list)

    assert updated_songs_counter == 1
    assert len(page_list) == 1
    assert page_list[0] == elements_list
    

def test_process_elements_list_filter_command_genre_satisfied() -> None:
    # Test with /filter command where genre condition is satisfied
    command = "/filter"
    elements_list = [['Progressive Metalcore'], 'Australia', 'Bloodshot', 'Absence']
    query_genre = "progressive"
    release_genre = ["Progressive Metalcore"]
    query_country = ""
    release_country = "Australia"
    query_artist = ""
    release_artist = "Bloodshot"
    query_title = ""
    release_title = "Absence"
    songs_counter = 0
    total_songs = 5
    page_list = []

    updated_songs_counter, page_list = process_elements_list(command, elements_list, query_genre, release_genre,
                            query_country, release_country, query_artist,
                            release_artist, query_title, release_title,
                            songs_counter, total_songs, page_list)

    print("up   ", updated_songs_counter)
    assert updated_songs_counter == 1
    assert len(page_list) == 1
    assert page_list[0] == elements_list

def test_process_elements_list_filter_command_genre_not_satisfied() -> None:
    # Test with /filter command where genre condition is not satisfied
    command = "/filter -g-c"
    elements_list = ["progressive", "italy"]
    query_genre = "progressive"
    release_genre = ["progressive", "nu metal"]
    query_country = "italy"
    release_country = "italy"
    query_artist = ""
    release_artist = "unprocessed"
    query_title = ""
    release_title = "lore"
    songs_counter = 0
    total_songs = 5
    page_list = []

    updated_songs_counter, page_list = process_elements_list(command, elements_list, query_genre, release_genre,
                            query_country, release_country, query_artist,
                            release_artist, query_title, release_title,
                            songs_counter, total_songs, page_list)

    assert updated_songs_counter == 0
    assert len(page_list) == 0

# Add more test cases for other scenarios as needed

