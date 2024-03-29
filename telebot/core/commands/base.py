from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands = [BotCommand(command="menu", description="Главное меню")]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot(bot: Bot) -> None:
    await set_commands(bot)
