from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


async def start_chat(call: CallbackQuery, state: FSMContext):
    await state.set_state("in_support")
    await call.message.edit_text('Пиши в чат всё, что хочешь')


def register_chats(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_chat,
        text="chat"
    )
