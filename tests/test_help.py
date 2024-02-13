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
        text = "Here is a list of commands you can use:\n\n" \
            "/all [n]: returns information about the last n releases, without applying any filter on the releases. " \
            "If n is not specified, the last 20 releases will be returned;\n\n" \
            "/filter -[atgc] [\"artist\", \"title\", \"[genre1+genre2+...+genren], \"country\"] [n]: returns information about the last n releases, " \
            "applying the filters specified in the command. If n is not specified, the last 20 releases will be returned;"
    )