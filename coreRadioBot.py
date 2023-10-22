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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ecco un elenco dei comandi che puoi usare:\n\n/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. Se n non è specificato, verrano restituite le ultime 10 release; \n\n /filters [titolo] [genere] [nazione] [n]: restituisce info relative alle ultime n release, applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;")


if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    wrongQuestion_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), wrongQuestion)

    help_handler = CommandHandler('help',help)
    application.add_handler(start_handler)
    application.add_handler(wrongQuestion_handler)
    application.add_handler(help_handler)

    application.run_polling()