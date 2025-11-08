from aiogram import F, Router
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, ContentType,
                           InlineKeyboardButton, CallbackQuery, FSInputFile, InputMediaPhoto, WebAppInfo, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.enums import consts
from bot.keyboards import menu
from bot.enums import desc
from bot.states.state import Docs
from database.methods import UserMethods

router = Router()

@router.message(CommandStart())
async def cmd_menu(message: Message):
    # user = UserMethods()
    # if await user.is_user_exists(telegram_id=message.from_user.id):
    #     await user.add_user(message.from_user)
    await message.answer(text=consts.START_MESSAGE, reply_markup=menu.get_start_keyboard())



