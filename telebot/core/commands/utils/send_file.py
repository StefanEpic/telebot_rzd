from aiogram.types import Message, URLInputFile

from config import SITE_URL

NUMBER_TO_NAME = {
    '01': 'instructions',
    '02': 'ksot_p',
    '03': 'knowledge_test_schedules',
    '04': 'knowledge_test_forms',
    '05': 'magazine_design_examples',
    '06': 'sok',
    '07': 'application_forms',
    '08': 'technical_studies',
    '09': 'reminders',
    '10': 'normative_documents',
    '11': 'fire_safety'
}

NAME_TO_ANSWER = {
    '01': 'Инструкции',
    '02': 'КСОТ-П',
    '03': 'Графики проверки знаний',
    '04': 'Билеты для проверки знаний',
    '05': 'Примеры оформления журналов',
    '06': 'СОК',
    '07': 'Бланки заявлений',
    '08': 'Техническая учеба',
    '09': 'Памятки',
    '10': 'Нормативная документация',
    '11': 'Пожарная безопасность'
}


NAME_TO_NUMBER = {
    'instructions': '01',
    'ksot_p': '02',
    'knowledge_test_schedules': '03',
    'knowledge_test_forms': '04',
    'magazine_design_examples': '05',
    'sok': '06',
    'application_forms': '07',
    'technical_studies': '08',
    'reminders': '09',
    'normative_documents': '10',
    'fire_safety': '11'
}


async def get_document(dir_name: str, file_name: str, message: Message):
    url = f'http://{SITE_URL}/media/{NUMBER_TO_NAME[dir_name]}/{file_name}'
    document = URLInputFile(url=url, filename=file_name)
    await message.reply_document(document=document)
