import sys
sys.path.insert(1,'C:/Users/smbsv/Desktop/xCoreBot')
from src.coreRadioBot import wrong_question
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_help():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()

    await wrong_question(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text = "I didn't understand ...\nuse the command /help to discover which commands you can use!"
    )