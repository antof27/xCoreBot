from strings_operations import lower_case
from genre_checker import is_genre_satisfied

def process_elements_list(command, elements_list, query_genre, release_genre,
                            query_country, release_country, query_artist,
                            release_artist, query_title, release_title,
                            songs_counter, total_songs, page_list):
    """
    Process a list of elements based on the given   
    command and conditions, and append to the page list.

    Args:
        command (str): The command (/all or /filter).
        elements_list (list): List of music information elements.
        query_genre (str): The query genre.
        release_genre (list): List of release genres.
        query_country (str): The query country.
        release_country (str): The release country.
        query_artist (str): The query artist.
        release_artist (str): The release artist.
        query_title (str): The query title.
        release_title (str): The release title.
        songs_counter (int): Counter for the songs.
        total_songs (int): Total number of songs to scrape.
        page_list (list): The list to append the processed elements.

    Returns:
        int: Updated songs counter.
    """
    if all(elements_list):
        if command == "/all":
            if songs_counter <= total_songs:
                songs_counter += 1
            page_list.append(elements_list)
        elif command == "/filter":
            # Initialize a flag to check if at least one condition is satisfied
            genre_satisfied = is_genre_satisfied(query_genre, release_genre)

            if (query_country and lower_case(query_country) != lower_case(release_country)) or \
                (query_artist and lower_case(query_artist) != lower_case(release_artist)) or \
                (query_title and lower_case(query_title) != lower_case(release_title)):
                 songs_counter += 1
                 return songs_counter

            # Append to the list if at least one condition is satisfied and songs_counter is within limit
            songs_counter += 1
            if genre_satisfied and songs_counter <= total_songs:
                page_list.append(elements_list)
                
    return songs_counter
