from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.enums import consts


def get_keyboard():
    keyboard = [
        [InlineKeyboardButton(text=consts.PROFILE, callback_data="profile")],
        [InlineKeyboardButton(text=consts.TEST, callback_data="test")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup