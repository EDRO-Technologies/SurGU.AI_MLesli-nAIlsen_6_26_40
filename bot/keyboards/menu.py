from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.enums import consts

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=consts.PROFILE, callback_data="profile"),
     InlineKeyboardButton(text=consts.TEST, callback_data="test")],
     [InlineKeyboardButton(text=consts.COURSES, callback_data="courses"),
      InlineKeyboardButton(text=consts.MINI_APP, callback_data="mini-app")]
])