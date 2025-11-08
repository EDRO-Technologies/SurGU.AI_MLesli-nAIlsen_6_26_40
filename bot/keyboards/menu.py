from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.enums import consts


def get_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="Пройти тест", callback_data="test")],
        [InlineKeyboardButton(text="Добавить CSV историю ответов студента", callback_data="csv_document")],
        [InlineKeyboardButton(text="Добавить файлы от преподавателя", callback_data="asdasdsa")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup