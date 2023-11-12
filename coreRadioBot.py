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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ecco un elenco dei comandi che puoi usare:\n\n/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. Se n non è specificato, verrano restituite le ultime 10 release; \n\n /filter [titolo] [autore] [genere] [n]: restituisce info relative alle ultime n release, applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;")

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire uno solo! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = {"title": "song1", "authors": ["Gianni"], "genres": ["rap,pop,rock,hard rock"]}
    simList2 = {"title": "song2", "authors": ["Pippo","Pluto"], "genres": ["hard rock,rock"]}
    simList3 = {"title": "song3", "authors": ["Paperino"], "genres": ["rap,pop"]}
    simList4 = {"title": "song4", "authors": ["Topolino"], "genres": ["rock", "jazz", "blues"]}
    simList5 = {"title": "song5", "authors": ["Minnie"], "genres": ["pop", "country"]}
    simList6 = {"title": "song6", "authors": ["Paperoga"], "genres": ["hip-hop", "rap"]}
    simList7 = {"title": "song7", "authors": ["Pluto"], "genres": ["metal", "electronic"]}
    simList8 = {"title": "song8", "authors": ["Clarabella"], "genres": ["classical", "folk"]}
    simList9 = {"title": "song9", "authors": ["Archimede"], "genres": ["reggae", "soul"]}
    simList10 = {"title": "song10", "authors": ["Basettoni"], "genres": ["disco", "funk"]}
    simList11 = {"title": "song11", "authors": ["Nonna Papera"], "genres": ["indie", "alternative"]}
    simList12 = {"title": "song12", "authors": ["Gastone"], "genres": ["punk", "experimental"]}
    simList13 = {"title": "song13", "authors": ["Ugo"], "genres": ["trance", "ambient"]}


    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]

    if len(context.args)==0:
        if (10>len(songs)):
            for i in range(0,10):
                text = "song "+str(i)+"\nTitolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Canzoni terminate!")

        else:
            for i in range(0,10):
                text = "song "+str(i)+"\nTitolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

        
    else:
        if (int(context.args[0])>len(songs)):
            for i in range(0,len(songs)):
                text = "song "+str(i)+"\nTitolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Canzoni terminate!")

        else:
            for i in range(0,int(context.args[0])):
                text = "song "+str(i)+"\nTitolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)





async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args)>4:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hai inserito "+str(len(context.args))+" parametri, mentre ne devi inserire al più quattro! Usa /help per avere informazioni su come usare i vari comandi!")
        return

    # let's simulate lists with info about some songs

    simList1 = {"title": "song1", "authors": ["Gianni"], "genres": ["rap","pop","rock","hard rock"]}
    simList2 = {"title": "song2", "authors": ["Pippo","Pluto"], "genres": ["hard rock","rock"]}
    simList3 = {"title": "song3", "authors": ["Paperino"], "genres": ["rap","pop"]}
    simList4 = {"title": "song4", "authors": ["Topolino"], "genres": ["rock", "jazz", "blues"]}
    simList5 = {"title": "song5", "authors": ["Minnie"], "genres": ["pop", "country"]}
    simList6 = {"title": "song6", "authors": ["Paperoga"], "genres": ["hip-hop", "rap"]}
    simList7 = {"title": "song7", "authors": ["Pluto"], "genres": ["metal", "electronic", "pop"]}
    simList8 = {"title": "song8", "authors": ["Clarabella"], "genres": ["classical", "folk"]}
    simList9 = {"title": "song9", "authors": ["Archimede"], "genres": ["reggae", "soul"]}
    simList10 = {"title": "song10", "authors": ["Basettoni"], "genres": ["pop","disco", "funk","pop"]}
    simList11 = {"title": "song11", "authors": ["Nonna Papera"], "genres": ["indie", "alternative"]}
    simList12 = {"title": "song12", "authors": ["Gastone"], "genres": ["punk", "experimental","pop"]}
    simList13 = {"title": "song13", "authors": ["Ugo"], "genres": ["trance", "ambient","pop"]}

    songs = [simList1,simList2,simList3,simList4,simList5,simList6,simList7,simList8,simList9,simList10,simList11,simList12,simList13]
    
    filters = {"title":context.args[0].split('-'),"authors":context.args[1].split('-'),"genres":context.args[2].split('-')}

    if len(context.args) < 4 :
        count = 0
        for i in range(0,len(songs)):
            if count == 10:
                break
            if  any(elem in songs[i]["title"] for elem in filters["title"]) or any(elem in songs[i]["authors"] for elem in filters["authors"]) or any(elem in songs[i]["genres"] for elem in filters["genres"]):
                text = "Titolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                count = count+1

    else:
        count = 0
        for i in range(0,len(songs)):
            if count == int(context.args[3]):
                break
            if  any(elem in songs[i]["title"] for elem in filters["title"]) or any(elem in songs[i]["authors"] for elem in filters["authors"]) or any(elem in songs[i]["genres"] for elem in filters["genres"]):
                text = "Titolo: "+songs[i]["title"]+"\nAutori: "+', '.join(songs[i]["authors"])+"\nGeneri: "+', '.join(songs[i]["genres"])
                await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                count = count+1


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