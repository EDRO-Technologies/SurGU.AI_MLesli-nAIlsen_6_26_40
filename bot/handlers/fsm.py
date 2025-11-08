from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup
from bot.fsm.states import Analyzer, Parser
from ai_agent.yandex_gpt import generate_comp_profile, generate_theme_blocks
from bot.keyboards import menu
import csv
from utils import parser
import io

router = Router()


@router.message(Analyzer.active_analyzer_page)
async def _(message: Message, state: FSMContext):
    document = message.document
    if not message.document:
        return await message.answer(text="Вы прислали не документ.")
    file_name = document.file_name.lower()
    if not file_name.endswith(".csv"):
        return await message.answer(text="Неверный формат файла. Требуется формат .csv")
    await message.answer("Начинаю анализ Ваших тестов...")
    file = await message.bot.download(file=document.file_id, destination=io.BytesIO())
    file.seek(0)  # Возвращаем курсор в начало файла

    # Читаем CSV
    decoded_file = io.TextIOWrapper(file, encoding='utf-8')
    reader = csv.reader(decoded_file)
    data = str(list(reader))
    response_model = generate_comp_profile(data)

    return await message.answer(text=response_model, parse_mode="html", reply_markup=menu.get_back_keyboard())


@router.message(Parser.active_parser_page)
async def _(message: Message, state: FSMContext):
    document = message.document
    if not message.document:
        return await message.answer(text="Вы прислали не документ.")
    file_name = document.file_name.lower()
    if (not file_name.endswith(".pdf")) and (not file_name.endswith(".docx")):
        return await message.answer(text="Неверный формат файла. Требуется формат .docx, .pdf")
    await message.answer("Начинаю анализ Вашего материала...")
    file_bytes = io.BytesIO()
    file = await message.bot.download(file=document.file_id, destination=file_bytes)
    file.seek(0)  # Возвращаем курсор в начало файла

    # decoded_file = io.TextIOWrapper(file, encoding='utf-8')
    response = str()
    if file_name.endswith(".pdf"):
        content = parser.read_pdf(file_bytes)
        response = generate_theme_blocks(content)
    if file_name.endswith(".docx"):
        ...

    return await message.answer(text=response, parse_mode="markdown", reply_markup=menu.get_back_keyboard())
