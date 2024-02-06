#xCoreBot - module "Bot"

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import sys
sys.path.insert(1,'..')
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao "+str(user)+", sono xCoreBot!\nSono un bot che permette di ottenere info sulle ultime release nell'ambito della musica Metal.Usa il comando '/help' per scoprire quali sono i comandi che puoi utilizzare!")

async def wrong_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Non ho capito ...\nusa il comando /help per scoprire quali sono i comandi che puoi utilizzare!"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text = "Ecco un elenco dei comandi che puoi usare:\n\n" \
            "/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. " \
            "Se n non è specificato, verrano restituite le ultime 10 release; \n\n" \
            "/filter artista titolo genere1-genere2-...-genereN country [n]: restituisce info relative alle ultime n release, " \
            "applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;"

)
                               
async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire uno solo! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    sim_list_1 = ["Gianni", "song1", ["rap", "pop", "rock", "hard rock"], "Italy"]
    sim_list_2 = ["Pippo", "song2", ["hard rock", "rock"], "England"]
    sim_list_3 = ["Paperino", "song3", ["rap", "pop"], "Denmark"]
    sim_list_4 = ["Topolino", "song4", ["rock", "jazz", "blues"], "Italy"]
    sim_list_5 = ["Minnie", "song5", ["pop", "country"], "Italy"]
    sim_list_6 = ["Paperoga", "song6", ["hip-hop", "rap"], "Italy"]
    sim_list_7 = ["Pluto", "song7", ["metal", "electronic", "pop"], "USA"]
    sim_list_8 = ["Clarabella", "song8", ["classical", "folk"], "England"]
    sim_list_9 = ["Archimede", "song9", ["reggae", "soul"], "Germany"]
    sim_list_10 = ["Basettoni", "song10", ["pop", "disco", "funk", "pop"], "Korea"]
    sim_list_11 = ["Nonna Papera", "song11", ["indie", "alternative"], "Poland"]
    sim_list_12 = ["Gastone", "song12", ["punk", "experimental", "pop"], "Poland"]
    sim_list_13 = ["Ugo", "song13", ["trance", "ambient", "pop"], "USA"]

    songs = [sim_list_1,
             sim_list_2,
             sim_list_3,
             sim_list_4,
             sim_list_5,
             sim_list_6,
             sim_list_7,
             sim_list_8,
             sim_list_9,
             sim_list_10,
             sim_list_11,
             sim_list_12,
             sim_list_13]

    count = 0
    limit = 10 if len(context.args) == 0 else int(context.args[0])
    text = ""

    for song in songs:
        if count == limit:
            break

        text = text + f"Titolo: {song[1]}\nArtista: {song[0]}\nCountry: {song[3]}\nGeneri: {', '.join(song[2])}\n\n"
        count += 1

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>5:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire cinque! Usa /help per avere informazioni su come usare i vari comandi!")
        return
    if len(context.args)<4:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri ... tutti i parametri sono obbligatori! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    sim_list_1 = ["Gianni", "song1", ["rap", "pop", "rock", "hard rock"], "Italy"]
    sim_list_2 = ["Pippo", "song2", ["hard rock", "rock"], "England"]
    sim_list_3 = ["Paperino", "song3", ["rap", "pop"], "Denmark"]
    sim_list_4 = ["Topolino", "song4", ["rock", "jazz", "blues"], "Italy"]
    sim_list_5 = ["Minnie", "song5", ["pop", "country"], "Italy"]
    sim_list_6 = ["Paperoga", "song6", ["hip-hop", "rap"], "Italy"]
    sim_list_7 = ["Pluto", "song7", ["metal", "electronic", "pop"], "USA"]
    sim_list_8 = ["Clarabella", "song8", ["classical", "folk"], "England"]
    sim_list_9 = ["Archimede", "song9", ["reggae", "soul"], "Germany"]
    sim_list_10 = ["Basettoni", "song10", ["pop", "disco", "funk", "pop"], "Korea"]
    sim_list_11 = ["Nonna Papera", "song11", ["indie", "alternative"], "Poland"]
    sim_list_12 = ["Gastone", "song12", ["punk", "experimental", "pop"], "Poland"]
    sim_list_13 = ["Ugo", "song13", ["trance", "ambient", "pop"], "USA"]


    songs = [sim_list_1,sim_list_2,sim_list_3,sim_list_4,sim_list_5,sim_list_6,sim_list_7,sim_list_8,sim_list_9,sim_list_10,sim_list_11,sim_list_12,sim_list_13]
    filters = {"artist":context.args[0], "title":context.args[1], "genres":context.args[2].split('-'), "country":context.args[3]}

    limit = 10 if len(context.args) < 5 else int(context.args[4])
    filtered_songs = [
        song for song in songs
        if song[0] == filters["artist"]
        and song[1] == filters["title"]
        and song[3] == filters["country"]
        and any(elem in song[2] for elem in filters["genres"])
    ]

    count = 0
    text = ""
    for song in filtered_songs[:limit]:
        text = text + f"Titolo: {song[1]}\nArtista: {song[0]}\nCountry: {song[3]}\nGeneri: {', '.join(song[2])}"
        count += 1

    if count == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Nessun risultato trovato...")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

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