import sys
sys.path.insert(1,'C:/Users/smbsv/Desktop/xCoreBot')
from src.coreRadioBot import start
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_start():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    update.message.from_user.username = "user_test"

    await start(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Ciao user_test, sono xCoreBot!\nSono un bot che permette di ottenere info sulle ultime release nell'ambito della musica Metal.Usa il comando '/help' per scoprire quali sono i comandi che puoi utilizzare!"
    )