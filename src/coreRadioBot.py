"""
xCoreBot - Module for Metal Music Genre Bot

This module contains functionality for a Telegram bot named xCoreBot.
The bot provides information about the latest releases in the Metal music genre.

Functions:
- start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Sends a greeting message to the user when they start interacting with the bot.

- wrong_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Handles unrecognized commands or messages by providing guidance on how to use the bot.

- help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Provides a list of available commands and their usage instructions.

- print_query_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Retrieves query results based on the user's input command and sends them as messages.

- split_message(text, max_length=4096):
  Utility function to split a long message into smaller chunks for sending.

- all(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Handles the '/all' command by extracting arguments, checking their validity,
  and printing query results.

- filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
  Handles the '/filter' command by extracting arguments, checking their validity,
  and printing query results.

- main:
  Entry point of the module, sets up the bot's handlers and starts the polling loop.

#Run Pylint with the following command: pylint --disable=C0301,E0401,C0103 coreRadioBot.py
#The import-error can be ignored as it is a false negative error
"""
import os
import sys
import yaml
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


# with open("token_config.yaml", 'r') as stream:
#     config = yaml.safe_load(stream)

      
# TOKEN = config['TOKEN']

TOKEN = os.environ.get('TOKEN')

if TOKEN is None:
    raise ValueError("The token is not set. Please set the token in the environment variable TOKEN")

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)
from src.coreradio_scraper import query_results
from src.token_extractor import arguments_checker


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a greeting message to the user upon starting interaction with the bot.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
    user = update.message.from_user.username
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hello " + str(user)+", I'm xCoreBot!\nI'm a bot that provides information about the latest releases in the Metal music genre. Use the command '/help' to discover the commands you can use!")


async def wrong_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a message indicating that the bot couldn't understand the user's input.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I didn't understand ...\nuse the command /help to discover which commands you can use!"
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Provide help information to the user by sending a message with a list of available commands and their usage.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Here is a list of commands you can use:\n\n" \
            "/all [n]: returns information about the last n releases, without applying any filter on the releases. " \
            "If n is not specified, the last 20 releases will be returned;\n\n" \
            "/filter -[atgc] [\"artist\", \"title\", \"[genre1+genre2+...+genren], \"country\"] [n]: returns information about the last n releases, " \
            "applying the filters specified in the command. If n is not specified, the last 20 releases will be returned;"
    )


async def print_query_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Process and print the query results to the chat.

    Retrieves the query results based on the input message text, constructs
    messages for each song with their details, and sends them to the chat.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
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

    for msg in messages:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def split_message(text, max_length=4096):
    """
    Split a message into smaller chunks to ensure it doesn't exceed a maximum length.

    Args:
        text (str): The message text to be split into chunks.
        max_length (int, optional): The maximum length of each chunk. Defaults to 4096.

    Returns:
        list: A list of message chunks, where each chunk has a maximum length of max_length.
    """
    if len(text) <= max_length:
        return [text]
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    return chunks





async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the '/all' command by retrieving query arguments, checking their validity,
    and printing query results.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
    # Extracting arguments using tuple unpacking
    c, f, v, n = arguments_checker(update.message.text)
    # Checking if all arguments are None
    if c is None and f is None and v is None and n is None:
        await wrong_question(update, context)
        return
    await print_query_results(update, context)



async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the '/filter' command by retrieving query arguments, checking their validity,
    and printing query results.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): The context object used for interacting with the Telegram Bot API.

    Returns:
        None
    """
    # Extracting arguments using tuple unpacking
    c, f, v, n = arguments_checker(update.message.text)
    # Checking if all arguments are None
    if c is None and f is None and v is None and n is None:
        await wrong_question(update, context)
        return
    await print_query_results(update, context)




if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    wrongQuestion_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), wrong_question)
    help_handler = CommandHandler('help',help)
    all_handler = CommandHandler('all', all)
    filter_handler = CommandHandler('filter', filter)

    application.add_handler(start_handler)
    application.add_handler(wrongQuestion_handler)
    application.add_handler(help_handler)
    application.add_handler(all_handler)
    application.add_handler(filter_handler)
    application.run_polling()
