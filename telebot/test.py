import httpx
import os
from aiogram import Bot, Dispatcher, types

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data.startswith('download_and_send_file_'))
async def download_and_send_file_callback(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    file_url = callback_query.data.split('_')[3]  # Получаем URL файла из данных CallbackQuery

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(file_url)
            if response.status_code == 200:
                file_name = os.path.basename(file_url)  # Получаем имя файла из URL
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                with open(file_name, 'rb') as file:
                    await bot.send_document(chat_id, file)
            else:
                await bot.send_message(chat_id, "Не удалось скачать файл.")
        except Exception as e:
            await bot.send_message(chat_id, f"Произошла ошибка: {str(e)}")

    # Ответьте на CallbackQuery, чтобы закрыть всплывающее уведомление
    await callback_query.answer()


async def send_download_links(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="Скачать файл 1",
            callback_data="download_file_1"
        ),
        types.InlineKeyboardButton(
            text="Скачать файл 2",
            callback_data="download_file_2"
        ),
    )

    await bot.send_message(
        chat_id,
        "Выберите файл для скачивания:",
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )