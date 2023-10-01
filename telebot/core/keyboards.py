from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.commands.utils.callback_factory import Menu, DownloadFile
from core.commands.utils.send_file import NAME_TO_NUMBER


def menu_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🗂 Охрана труда',
                            callback_data='occupational_safety_and_health')
    keyboard_builder.button(text='📁 Бланки заявлений',
                            callback_data=Menu(title='07', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Техническая учеба',
                            callback_data=Menu(title='08', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Памятки',
                            callback_data=Menu(title='09', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Нормативная документация',
                            callback_data=Menu(title='10', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Пожарная безопасность',
                            callback_data=Menu(title='11', page=1, need_pagination=False))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def safety_and_health_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='📁 Инструкции',
                            callback_data=Menu(title='01', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 КСОТ-П',
                            callback_data=Menu(title='02', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 График проверки знаний',
                            callback_data=Menu(title='03', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Билеты для проверки знаний',
                            callback_data=Menu(title='04', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 Примеры оформления журналов',
                            callback_data=Menu(title='05', page=1, need_pagination=False))
    keyboard_builder.button(text='📁 СОК',
                            callback_data=Menu(title='06', page=1, need_pagination=False))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def list_keyboard(data: dir, dir_name: str, current_page: int, page_count: int):
    keyboard_builder = InlineKeyboardBuilder()
    row = []

    for x in data['results']:
        file = x['file'].split('/')
        file_name = file[-1]
        download_dir_name = NAME_TO_NUMBER[file[-2]]
        keyboard_builder.button(text=f'📄 {x["title"]}',
                                callback_data=DownloadFile(title=download_dir_name, file=file_name))
        row.append(1)

    if page_count > 1:
        if current_page != 1:
            keyboard_builder.button(text=f'⬅️',
                                    callback_data=Menu(title=dir_name, page=current_page - 1, need_pagination=True))

        else:
            keyboard_builder.button(text=f'⛔️', callback_data='stop')

        keyboard_builder.button(text=f'{current_page}/{page_count}', callback_data='stop')

        if current_page == page_count:
            keyboard_builder.button(text=f'⛔️', callback_data='stop')
        else:
            keyboard_builder.button(text=f'➡️',
                                    callback_data=Menu(title=dir_name, page=current_page + 1, need_pagination=True))

        row.append(3)
    keyboard_builder.adjust(*row)

    return keyboard_builder.as_markup()
