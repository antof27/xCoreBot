import logging
import config
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao, sono xCoreBot!\nSono un bot che permette di ottenere info sulle ultime release nell'ambito della musica Metal. Usa il comando '/help' per scoprire quali sono i comandi che puoi utilizzare!")

async def wrongQuestion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Non ho capito ... usa il comando /help per scoprire quali sono i comandi che puoi utilizzare!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ecco un elenco dei comandi che puoi usare:\n\n/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. Se n non è specificato, verrano restituite le ultime 10 release; \n\n /filter artista titolo genere1-genere2-...-genereN country [n]: restituisce info relative alle ultime n release, applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;")

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire uno solo! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = ["Gianni", "song1", ["rap", "pop", "rock", "hard rock"], "Italy"]
    simList2 = ["Pippo", "song2", ["hard rock", "rock"], "England"]
    simList3 = ["Paperino", "song3", ["rap", "pop"], "Denmark"]
    simList4 = ["Topolino", "song4", ["rock", "jazz", "blues"], "Italy"]
    simList5 = ["Minnie", "song5", ["pop", "country"], "Italy"]
    simList6 = ["Paperoga", "song6", ["hip-hop", "rap"], "Italy"]
    simList7 = ["Pluto", "song7", ["metal", "electronic", "pop"], "USA"]
    simList8 = ["Clarabella", "song8", ["classical", "folk"], "England"]
    simList9 = ["Archimede", "song9", ["reggae", "soul"], "Germany"]
    simList10 = ["Basettoni", "song10", ["pop", "disco", "funk", "pop"], "Korea"]
    simList11 = ["Nonna Papera", "song11", ["indie", "alternative"], "Poland"]
    simList12 = ["Gastone", "song12", ["punk", "experimental", "pop"], "Poland"]
    simList13 = ["Ugo", "song13", ["trance", "ambient", "pop"], "USA"]

    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]

    count = 0
    limit = 10 if len(context.args) == 0 else int(context.args[0])

    for song in songs:
        if count == limit:
            break

        text = f"Titolo: {song[1]}\nArtista: {song[0]}\nCountry: {song[3]}\nGeneri: {', '.join(song[2])}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        count += 1


async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>5:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire al più cinque! Usa /help per avere informazioni su come usare i vari comandi!")
        return
    
    if len(context.args)<4:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri ... tutti i parametri sono obbligatori! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = ["Gianni", "song1", ["rap", "pop", "rock", "hard rock"], "Italy"]
    simList2 = ["Pippo", "song2", ["hard rock", "rock"], "England"]
    simList3 = ["Paperino", "song3", ["rap", "pop"], "Denmark"]
    simList4 = ["Topolino", "song4", ["rock", "jazz", "blues"], "Italy"]
    simList5 = ["Minnie", "song5", ["pop", "country"], "Italy"]
    simList6 = ["Paperoga", "song6", ["hip-hop", "rap"], "Italy"]
    simList7 = ["Pluto", "song7", ["metal", "electronic", "pop"], "USA"]
    simList8 = ["Clarabella", "song8", ["classical", "folk"], "England"]
    simList9 = ["Archimede", "song9", ["reggae", "soul"], "Germany"]
    simList10 = ["Basettoni", "song10", ["pop", "disco", "funk", "pop"], "Korea"]
    simList11 = ["Nonna Papera", "song11", ["indie", "alternative"], "Poland"]
    simList12 = ["Gastone", "song12", ["punk", "experimental", "pop"], "Poland"]
    simList13 = ["Ugo", "song13", ["trance", "ambient", "pop"], "USA"]


    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]
    
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
    for song in filtered_songs[:limit]:
        text = f"Titolo: {song[1]}\nArtista: {song[0]}\nCountry: {song[3]}\nGeneri: {', '.join(song[2])}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        count += 1

    if count == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Nessun risultato trovato...")

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    wrongQuestion_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), wrongQuestion)
    help_handler = CommandHandler('help',help)
    all_handler = CommandHandler('all', all)
    filter_handler = CommandHandler('filter', filter)

    application.add_handler(start_handler)
    application.add_handler(wrongQuestion_handler)
    application.add_handler(help_handler)
    application.add_handler(all_handler)
    application.add_handler(filter_handler)

    application.run_polling()