import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from core.commands.base import start_bot
from core.commands.callback import safety_and_health, get_list, download_file
from core.commands.commands import start, menu
from core.commands.utils.callback_factory import Menu, DownloadFile


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.startup.register(start_bot)
    dp.message.register(start, Command(commands='start'))
    dp.message.register(menu, Command(commands='menu'))

    dp.callback_query.register(safety_and_health, F.data.startswith('occupational_safety_and_health'))
    dp.callback_query.register(get_list, Menu.filter())
    dp.callback_query.register(download_file, DownloadFile.filter())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
