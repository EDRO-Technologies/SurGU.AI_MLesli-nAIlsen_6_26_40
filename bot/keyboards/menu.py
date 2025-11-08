from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.enums import consts


def get_start_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="🤣 Профиль", callback_data="profile_menu")],
        [InlineKeyboardButton(text="⚙️ Анализатор тестов", callback_data="analyz_menu"),
         InlineKeyboardButton(text="🗣️ Парсер документов", callback_data="parser_menu")],
        [InlineKeyboardButton(text="💣 Генерация контента", callback_data="generate_content_menu")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup

def get_analyzer_start_keyboard():
    keyboard = [[InlineKeyboardButton(text="Начать анализ", callback_data="start_analyz")],
                [InlineKeyboardButton(text="Назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup

def get_parse_start_keyboard():
    keyboard = [[InlineKeyboardButton(text="Начать парсинг", callback_data="start_parse")],
                [InlineKeyboardButton(text="Назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup

def get_cancel_keyboard():
    keyboard = [[InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup

def get_back_keyboard():
    keyboard = [[InlineKeyboardButton(text="🏃‍♂️ Вернуться в главное меню", callback_data="back")]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup