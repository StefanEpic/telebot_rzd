from math import ceil

import requests
from aiogram.types import CallbackQuery

from config import SITE_URL
from core.commands.utils.callback_factory import Menu, DownloadFile
from core.commands.utils.send_file import (
    get_document,
    NAME_TO_ANSWER,
    NUMBER_TO_NAME,
)
from core.keyboards import safety_and_health_keyboard, list_keyboard


async def safety_and_health(call: CallbackQuery) -> None:
    await call.message.answer(text="🤖 Охрана труда:", reply_markup=safety_and_health_keyboard())


async def get_list(call: CallbackQuery, callback_data: Menu) -> None:
    dir_name = NUMBER_TO_NAME[callback_data.title]
    page = callback_data.page
    url = f"http://{SITE_URL}/{dir_name}/?page={page}"

    response = requests.get(url)
    data = response.json()

    if callback_data.need_pagination:
        await call.message.edit_reply_markup(
            reply_markup=list_keyboard(
                data,
                callback_data.title,
                int(page),
                ceil(int(data["count"]) / 5),
            )
        )
    else:
        await call.message.answer(
            text=f"🤖 {NAME_TO_ANSWER[callback_data.title]}:",
            reply_markup=list_keyboard(
                data,
                callback_data.title,
                int(page),
                ceil(int(data["count"]) / 5),
            ),
        )


async def download_file(call: CallbackQuery, callback_data: DownloadFile) -> None:
    dir_name = callback_data.title
    file_name = callback_data.file
    await get_document(dir_name, file_name, call.message)
