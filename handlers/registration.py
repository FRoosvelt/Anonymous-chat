from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from db_api.commands.users import select_user_id, add_user


async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("📨Общение", callback_data="chat")
            ]
        ]
    )
    if not await select_user_id(message.from_user.id):
        await add_user(message.from_user.id)
        return await message.answer(
            "👋Добро пожаловать в анонимный чат! Здесь вы можете разговаривовать анонимно с разными людьми\n"
            "Чтобы начать разговаривать, нажми на кнопку", reply_markup=keyboard)
    elif await select_user_id(message.from_user.id):
        return await message.answer(
            "👋Добро пожаловать в анонимный чат! Здесь вы можете разговаривовать анонимно с разными людьми\n"
            "Чтобы начать разговаривать, нажми на кнопку")


def register_registration(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart()
    )
