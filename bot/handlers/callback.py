from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.enums import desc, consts
from bot.keyboards import menu
from bot.fsm.states import Page, Analyzer, Parser

router = Router()

@router.callback_query(F.data == 'analyz_menu')
async def _(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Page.test_analyzer_page)
    await cb.answer()
    await cb.message.answer(text=desc.ANALYZER_DESC, parse_mode='HTML', reply_markup=menu.get_analyzer_start_keyboard())

@router.callback_query(F.data == 'start_analyz')
async def _(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Analyzer.active_analyzer_page)
    await cb.answer()
    await cb.message.answer(text="Пришлите документ в формате .csv", parse_mode='HTML', reply_markup=menu.get_cancel_keyboard())


@router.callback_query(F.data == 'parser_menu')
async def _(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Page.parser_page)
    await cb.answer()
    await cb.message.answer(text=desc.PARSER_DESC, parse_mode='HTML', reply_markup=menu.get_parse_start_keyboard())


@router.callback_query(F.data == 'start_parse')
async def _(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Parser.active_parser_page)
    await cb.answer()
    await cb.message.answer(text="Пришлите документ в формате .pdf либо .docx.", parse_mode='HTML', reply_markup=menu.get_cancel_keyboard())
@router.callback_query(F.data == 'back')
async def document_msg(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Page.start_page)
    await cb.answer()
    await cb.message.answer(text=consts.START_MESSAGE, parse_mode='HTML', reply_markup=menu.get_start_keyboard())

@router.callback_query(F.data == 'cancel')
async def document_msg(cb: CallbackQuery, state: FSMContext):
    await cb.message.delete()
    await state.set_state(Page.start_page)
    await cb.answer("Действие отменено")
    await cb.message.answer(text=consts.START_MESSAGE, parse_mode='HTML', reply_markup=menu.get_start_keyboard())