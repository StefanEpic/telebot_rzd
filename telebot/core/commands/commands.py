from aiogram import types

from core.keyboards import menu_keyboard


async def start(message: types.Message) -> None:
    await message.reply(
        f"👋 Привет, {message.from_user.first_name}!\n🚂 Это бот ОДМС-3!\n\n🤖 Выбери раздел:",
        reply_markup=menu_keyboard(),
    )


async def menu(message: types.Message) -> None:
    await message.reply("🤖 Выбери раздел:", reply_markup=menu_keyboard())
