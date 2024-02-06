import sys
sys.path.insert(1,'C:/Users/smbsv/Desktop/xCoreBot')
from src.coreRadioBot import all
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_all_argument_1():
    update = Mock()
    context = Mock()
    context.args = ["1"] #Example: only the first song
    context.bot.send_message = AsyncMock()

    await all(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Titolo: song1\nArtista: Gianni\nCountry: Italy\nGeneri: rap, pop, rock, hard rock\n\n"
    )

@pytest.mark.asyncio
async def test_no_argument():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = [] #Example: no argument

    await all(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,

        # first 10 songs
        text="Titolo: song1\nArtista: Gianni\nCountry: Italy\nGeneri: rap, pop, rock, hard rock\n\n"+ \
                "Titolo: song2\nArtista: Pippo\nCountry: England\nGeneri: hard rock, rock\n\n"+ \
                "Titolo: song3\nArtista: Paperino\nCountry: Denmark\nGeneri: rap, pop\n\n"+ \
                "Titolo: song4\nArtista: Topolino\nCountry: Italy\nGeneri: rock, jazz, blues\n\n"+ \
                "Titolo: song5\nArtista: Minnie\nCountry: Italy\nGeneri: pop, country\n\n"+ \
                "Titolo: song6\nArtista: Paperoga\nCountry: Italy\nGeneri: hip-hop, rap\n\n"+ \
                "Titolo: song7\nArtista: Pluto\nCountry: USA\nGeneri: metal, electronic, pop\n\n"+ \
                "Titolo: song8\nArtista: Clarabella\nCountry: England\nGeneri: classical, folk\n\n"+ \
                "Titolo: song9\nArtista: Archimede\nCountry: Germany\nGeneri: reggae, soul\n\n"+ \
                "Titolo: song10\nArtista: Basettoni\nCountry: Korea\nGeneri: pop, disco, funk, pop\n\n"
    )

@pytest.mark.asyncio
async def test_all_too_many_argument():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.args = [1,2]

    
    await all(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Hai inserito 2 parametri, mentre ne devi inserire uno solo! Usa /help per avere informazioni su come usare i vari comandi!"
    )