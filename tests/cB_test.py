from unittest.mock import AsyncMock, MagicMock, Mock
import pytest
import os
import sys

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)
sys.path.insert(1, parent_directory)

from src.coreRadioBot import start, help, wrong_question
from src.coreradio_scraper import query_results
from telegram import Update
from telegram.ext import ContextTypes
import pytest


@pytest.mark.asyncio
async def test_start():
    update = Mock()
    # Mock the message attribute
    update.message = Mock()
    # Provide a username for the user
    update.message.from_user.username = "test_user"
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await start(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Hello test_user, I'm xCoreBot!\nI'm a bot that provides information about the latest releases in the Metal music genre. Use the command '/help' to discover the commands you can use!"
    )

@pytest.mark.asyncio
async def test_help():
    update = Mock()
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await help(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Here is a list of commands you can use:\n\n" \
            "/all [n]: returns information about the last n releases, without applying any filter on the releases. " \
            "If n is not specified, the last 20 releases will be returned;\n\n" \
            "/filter -[atgc] [\"artist\", \"title\", \"[genre1+genre2+...+genren], \"country\"] [n]: returns information about the last n releases, " \
            "applying the filters specified in the command. If n is not specified, the last 20 releases will be returned;"
    )

@pytest.mark.asyncio
async def test_wrong_question():
    update = Mock()
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await wrong_question(update, context)
    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="I didn't understand ...\nuse the command /help to discover which commands you can use!"
    )

# Reworked all function
async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Call query_results with "/all" command
    results = query_results("/all")
    # Print the results directly
    await context.bot.send_message(chat_id=update.effective_chat.id, text=results)

# Reworked filter function
async def filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Call query_results with the filter command from update.message.text
    results = query_results(update.message.text)
    # Print the results directly
    await context.bot.send_message(chat_id=update.effective_chat.id, text=results)

# Test for all function
@pytest.mark.asyncio
async def test_all():
    # Mock Update and ContextTypes objects
    update = Mock()
    context = MagicMock()
    # Mock query_results function
    query_results_mock = Mock()
    # Mock results returned by query_results
    mock_results = "Result for /all"
    query_results_mock.return_value = mock_results
    # Set update.message.text to "/all"
    update.message.text = "/all"
    
    # Call all function
    await all(update, context)

    # Ensure that query_results was called with the correct arguments
    query_results_mock.assert_called_once_with("/all")

    # Ensure that send_message was called with the correct arguments
    context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text=mock_results)

# Test for filter function
@pytest.mark.asyncio
async def test_filter():
    # Mock Update and ContextTypes objects
    update = Mock()
    context = MagicMock()
    # Mock query_results function
    query_results_mock = Mock()
    # Mock results returned by query_results
    mock_results = "Result for /filter -c USA 10"
    query_results_mock.return_value = mock_results
    # Set update.message.text to "/filter -c USA 10"
    update.message.text = "/filter -c USA 10"

    # Call filter function
    await filter(update, context)

    # Ensure that query_results was called with the correct arguments
    query_results_mock.assert_called_once_with("/filter -c USA 10")

    # Ensure that send_message was called with the correct arguments
    context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text=mock_results)
