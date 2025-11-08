from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.enums import consts


def get_keyboard():
    keyboard = [
        [InlineKeyboardButton(text=consts.PROFILE, callback_data="profile"),
         InlineKeyboardButton(text=consts.TEST, callback_data="test")],
         [InlineKeyboardButton(text="Добавить CSV историю ответов студента", callback_data="csv-document"),
          InlineKeyboardButton(text="Добавить файлы от преподавателя")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup