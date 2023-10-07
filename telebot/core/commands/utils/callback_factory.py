from aiogram.filters.callback_data import CallbackData


class Menu(CallbackData, prefix="menu"):
    title: str
    page: int
    need_pagination: bool


class DownloadFile(CallbackData, prefix="download"):
    title: str
    file: str
