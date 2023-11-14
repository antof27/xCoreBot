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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ecco un elenco dei comandi che puoi usare:\n\n/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. Se n non è specificato, verrano restituite le ultime 10 release; \n\n /filter artista titolo genere1-genere2-...-genereN n: restituisce info relative alle ultime n release, applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;")

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire uno solo! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = {"artist": "Gianni", "title": "song1", "genres": ["rap","pop","rock","hard rock"], "country":"Italy"}
    simList2 = {"artist": "Pippo", "title": "song2", "genres": ["hard rock","rock"], "country":"England"}
    simList3 = {"artist": "Paperino", "title": "song3", "genres": ["rap","pop"], "country":"Denmark"}
    simList4 = {"artist": "Topolino", "title": "song4", "genres": ["rock", "jazz", "blues"], "country":"Italy"}
    simList5 = {"artist": "Minnie", "title": "song5", "genres": ["pop", "country"], "country":"Italy"}
    simList6 = {"artist": "Paperoga", "title": "song6", "genres": ["hip-hop", "rap"], "country":"Italy"}
    simList7 = {"artist": "Pluto", "title": "song7", "genres": ["metal", "electronic", "pop"], "country":"USA"}
    simList8 = {"artist": "Clarabella","title": "song8", "genres": ["classical", "folk"], "country":"England"}
    simList9 = {"artist": "Archimede", "title": "song9", "genres": ["reggae", "soul"], "country":"Germany"}
    simList10 = {"artist": "Basettoni", "title": "song10","genres": ["pop","disco", "funk","pop"], "country":"Korea"}
    simList11 = {"artist": "Nonna Papera", "title": "song11", "genres": ["indie", "alternative"], "country":"Poland"}
    simList12 = {"artist": "Gastone", "title": "song12", "genres": ["punk", "experimental","pop"], "country":"Poland"}
    simList13 = {"artist": "Ugo", "title": "song13", "genres": ["trance", "ambient","pop"],  "country":"USA"}


    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]

    if len(context.args)==0:
        count = 0
        for i in range(0,len(songs)):
            if count == 10:
                break
            text = "Titolo: "+songs[i]["title"]+"\nArtista: "+songs[i]["artist"]+"\nCountry: "+songs[i]["country"]+"\nGeneri: "+', '.join(songs[i]["genres"])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            count = count+1

        
    else:
        count = 0
        for i in range(0,len(songs)):
            if count == int(context.args[0]):
                break
            text = "Titolo: "+songs[i]["title"]+"\nArtista: "+songs[i]["artist"]+"\nCountry: "+songs[i]["country"]+"\nGeneri: "+', '.join(songs[i]["genres"])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            count = count+1





async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>5:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire al più quattro! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = {"artist": "Gianni", "title": "song1", "genres": ["rap","pop","rock","hard rock"], "country":"Italy"}
    simList2 = {"artist": "Pippo", "title": "song2", "genres": ["hard rock","rock"], "country":"England"}
    simList3 = {"artist": "Paperino", "title": "song3", "genres": ["rap","pop"], "country":"Denmark"}
    simList4 = {"artist": "Topolino", "title": "song4", "genres": ["rock", "jazz", "blues"], "country":"Italy"}
    simList5 = {"artist": "Minnie", "title": "song5", "genres": ["pop", "country"], "country":"Italy"}
    simList6 = {"artist": "Paperoga", "title": "song6", "genres": ["hip-hop", "rap"], "country":"Italy"}
    simList7 = {"artist": "Pluto", "title": "song7", "genres": ["metal", "electronic", "pop"], "country":"USA"}
    simList8 = {"artist": "Clarabella","title": "song8", "genres": ["classical", "folk"], "country":"England"}
    simList9 = {"artist": "Archimede", "title": "song9", "genres": ["reggae", "soul"], "country":"Germany"}
    simList10 = {"artist": "Basettoni", "title": "song10","genres": ["pop","disco", "funk","pop"], "country":"Korea"}
    simList11 = {"artist": "Nonna Papera", "title": "song11", "genres": ["indie", "alternative"], "country":"Poland"}
    simList12 = {"artist": "Gastone", "title": "song12", "genres": ["punk", "experimental","pop"], "country":"Poland"}
    simList13 = {"artist": "Ugo", "title": "song13", "genres": ["trance", "ambient","pop"],  "country":"USA"}

    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]
    
    filters = {"artist":context.args[0], "title":context.args[1], "genres":context.args[2].split('-'), "country":context.args[3]}

    if len(context.args) < 5 :
        count = 0
        for i in range(0,len(songs)):
            if count == 10:
                break
            if  songs[i]["artist"]==filters["artist"] or songs[i]["title"]==filters["title"] or songs[i]["country"]==filters["country"] or all(elem in songs[i]["genres"] for elem in filters["genres"]):
                text = "Titolo: "+songs[i]["title"]+"\nArtista: "+songs[i]["artist"]+"\nCountry: "+songs[i]["country"]+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                count = count+1
        if count == 0:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Nessun risultato trovato...")

    else:
        count = 0
        for i in range(0,len(songs)):
            if count == int(context.args[4]):
                break
            if  songs[i]["artist"]==filters["artist"] or songs[i]["title"]==filters["title"] or songs[i]["country"]==filters["country"] or (all(elem in songs[i]["genres"] for elem in filters["genres"])):
                text = "Titolo: "+songs[i]["title"]+"\nArtista: "+songs[i]["artist"]+"\nCountry: "+songs[i]["country"]+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                count = count+1
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