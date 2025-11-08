from aiogram import F, Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, FSInputFile, InputMediaPhoto, WebAppInfo, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.enums import consts
from bot.keyboards import menu
from bot.middleware.register import Register

router = Router()
router.message.middleware(Register())

@router.message(CommandStart())
async def cmd_menu(message: Message):
    await message.answer(text=consts.START_MESSAGE, reply_markup=menu.get_keyboard())

@router.message(F.data == 'profile')
async def profle_message(message: Message):
    keyboard = ReplyKeyboardBuilder(resize_keyboard=True)
    button = KeyboardButton(
        text="Open Mini App",
        web_app=WebAppInfo(url="https://localhost:8080")
    )
    keyboard.add(button)
    await message.answer("Open Mini App:", reply_markup=keyboard)

@router.message(F.data == 'csv-document')
async def download_document(message: Message, state: FSMContext):
    await state.set_state()
    file_id = message.document.file_id
    file = await message.bot.get_file(file_id)
    await message.bot.download_file(file_path=file.file_path, destination="temp/")
