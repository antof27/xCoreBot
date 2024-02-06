import sys
sys.path.insert(1,'C:/Users/smbsv/Desktop/xCoreBot')
from src.coreRadioBot import filter
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_filter_less_arguments():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["Paperoga","song6"] #Example: only 2 arguments


    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text = "Hai inserito 2 parametri ... tutti i parametri sono obbligatori! Usa /help per avere informazioni su come usare i vari comandi!"
    )

@pytest.mark.asyncio
async def test_filter_more_arguments():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["Paperoga","song6","rap","Italy","China","Pippo"] #Example: only 2 arguments


    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text = "Hai inserito 6 parametri, mentre ne devi inserire cinque! Usa /help per avere informazioni su come usare i vari comandi!"
    )

@pytest.mark.asyncio
async def test_filter_find_results():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["Paperoga","song6","rap","Italy"] 

    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Titolo: song6\nArtista: Paperoga\nCountry: Italy\nGeneri: hip-hop, rap"
    )

@pytest.mark.asyncio
async def test_filter_no_results():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = ["Pippo","song13838882","noGenres","Antarctica"] 

    await filter(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Nessun risultato trovato..."
    )