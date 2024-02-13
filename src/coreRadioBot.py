#xCoreBot - module "Bot"

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import os
import sys

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)
from src.coreradio_scraper import query_results
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello "+str(user)+", I'm xCoreBot!\nI'm a bot that provides information about the latest releases in the Metal music genre. Use the command '/help' to discover the commands you can use!")


async def wrong_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I didn't understand ...\nuse the command /help to discover which commands you can use!"

    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is a list of commands you can use:\n\n" \
            "/all [n]: returns information about the last n releases, without applying any filter on the releases. " \
            "If n is not specified, the last 20 releases will be returned;\n\n" \
            "/filter -[atgc] [\"artist\", \"title\", \"[genre1+genre2+...+genren], \"country\"] [n]: returns information about the last n releases, " \
            "applying the filters specified in the command. If n is not specified, the last 20 releases will be returned;"
    )



async def print_query_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    messages.append("These are the results of your query, where the oldest songs are displayed first. Enjoy!")

    for msg in messages:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def split_message(text, max_length=4096):
    """Split a message into chunks."""
    if len(text) <= max_length:
        return [text]
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    return chunks


async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await print_query_results(update, context)

async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await print_query_results(update, context)



if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()
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