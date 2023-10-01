from aiogram import types

from core.keyboards import menu_keyboard


async def start(message: types.Message):
    await message.reply(
        f"👋 Привет, {message.from_user.first_name}!"
        f"\n🚂 Это бот ОДМС-3!\n"
        f"\n🤖 Выбери раздел:",
        reply_markup=menu_keyboard()
    )


async def menu(message: types.Message):
    await message.reply(
        '🤖 Выбери раздел:',
        reply_markup=menu_keyboard()
    )
