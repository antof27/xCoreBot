import sys
sys.path.insert(1,'C:/Users/smbsv/Desktop/xCoreBot')
from src.coreRadioBot import help
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_help():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()

    await help(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text = "Ecco un elenco dei comandi che puoi usare:\n\n" \
            "/all [n]: restituisce info relative alle ultime n release, senza applicare alcun filtro sulle release. " \
            "Se n non è specificato, verrano restituite le ultime 10 release; \n\n" \
            "/filter artista titolo genere1-genere2-...-genereN country [n]: restituisce info relative alle ultime n release, " \
            "applicando i filtri specificati nel comando. Se n non è specificato, verrano restituite le ultime 10 release;"
    )