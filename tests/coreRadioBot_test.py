from unittest.mock import AsyncMock, MagicMock, Mock
import pytest
import os
import sys
from typing import List

HELP = "Here is a list of commands you can use:\n\n" \
            "/all [n]: returns information about the last n releases, without applying any filter on the releases. " \
            "If n is not specified, the last 20 releases will be returned;\n\n" \
            "/filter -[atgc] [\"artist\", \"title\", \"[genre1+genre2+...+genren], \"country\"] [n]: returns information about the last n releases, " \
            "applying the filters specified in the command. If n is not specified, the last 20 releases will be returned;"

WRONG_QUESTION = "I didn't understand ...\nuse the command /help to discover which commands you can use!"

# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)
g_parent_directory: str = os.path.dirname(parent_directory)


sys.path.insert(1, parent_directory)
sys.path.insert(1, g_parent_directory)

from xCoreBot.__init__ import start, help, wrong_question, filter, all
from src.coreradio_scraper import query_results
import pytest

def split_message(text: str, max_length: int = 4096) -> List[str]:
    """Split a message into chunks."""
    if len(text) <= max_length:
        return [text]
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    return chunks



@pytest.mark.asyncio
async def test_start() -> None:
    update = Mock()
    # Mock the message attribute
    update.message = Mock()
    # Provide a username for the user
    update.message.from_user.username = "test_user"
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await start(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Hello test_user, I'm xCoreBot!\nI'm a bot that provides information about the latest releases in the Metal music genre. Use the command '/help' to discover the commands you can use!"
    )

@pytest.mark.asyncio
async def test_help() -> None:
    update = Mock()
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await help(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=HELP
    )

@pytest.mark.asyncio
async def test_wrong_question() -> None:
    update = Mock()
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await wrong_question(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )

@pytest.mark.asyncio
async def test_filter_less_arguments() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()  # Use AsyncMock for asynchronous function
    context.args = ["-gc", "Metalcore"]  # Example: only 2 arguments
    # Mocking the message text to be a real string
    update.message.text = "/filter -gc Metalcore"

    await filter(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )




@pytest.mark.asyncio
async def test_filter_one_argument() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["-a"] #Example: only 1 argument

    update.message.text = "/filter -a"

    await filter(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )


@pytest.mark.asyncio
async def test_filter_more_arguments() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["-gcat","metalcore","USA","artist4","Song","Other","Another"] #Example: too many arguments
    
    update.message.text = "/filter -gcat metalcore, USA, artist4, Song, Other, Another"

    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )

@pytest.mark.asyncio
async def test_filter_find_results() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["-c", "USA", "200"] 
    
    update.message.text = "/filter -c USA 200"

    songs = query_results(update.message.text)
    messages = []

    for song in songs:
        title = song[2]
        artist = song[3]
        country = song[1]
        genres = song[0]
        
        text = f"Title : {title}\nArtist : {artist}\nCountry : {country}\n"

        # Iterate genres and append to text
        text += "Genres : "
        for genre in genres:
            text += genre + ", "
        text = text[:-2]  # Remove the last comma and space
        text += "\n\n"

        messages.extend(split_message(text))

    if not messages:
        messages.append("No results found for your query. Try again with different filters.")
    else:
        messages.append("These are the results of your query, where the oldest songs are displayed first. Enjoy!")

    await filter(update, context)

    # Assert that send_message is called with each message in messages list
    for msg in messages:
        context.bot.send_message.assert_any_call(chat_id=update.effective_chat.id, text=msg)


@pytest.mark.asyncio
async def test_filter_no_results() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["-c","fakeCountry"] 
    
    update.message.text = "/filter -c fakeCountry"

    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="No results found for your query. Try again with different filters."
    )



@pytest.mark.asyncio
async def test_all_no_digit() -> None:
    update = Mock()
    context = Mock()
    context.args = ["Keyword"] #Example: only the first song
    context.bot.send_message = AsyncMock()

    update.message.text = "/all Keyword"

    await all(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )



@pytest.mark.asyncio
async def test_no_argument() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = [] #Example: no argument: return first 20 songs


    update.message.text = "/all"

    songs = query_results(update.message.text)
    messages = []

    for song in songs:
        title = song[2]
        artist = song[3]
        country = song[1]
        genres = song[0]
        
        text = f"Title : {title}\nArtist : {artist}\nCountry : {country}\n"

        # Iterate genres and append to text
        text += "Genres : "
        for genre in genres:
            text += genre + ", "
        text = text[:-2]  # Remove the last comma and space
        text += "\n\n"

        messages.extend(split_message(text))

    if not messages:
        messages.append("No results found for your query. Try again with different filters.")
    else:
        messages.append("These are the results of your query, where the oldest songs are displayed first. Enjoy!")

    await all(update, context)

    # Assert that send_message is called with each message in messages list
    for msg in messages:
        context.bot.send_message.assert_any_call(chat_id=update.effective_chat.id, text=msg)

        

@pytest.mark.asyncio
async def test_all_too_many_argument() -> None:
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["10", "20"]

    update.message.text = "/all 10 20"

    await all(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=WRONG_QUESTION
    )