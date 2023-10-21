from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import ParseMode

from data.config import TOKEN, storage
from db_api.commands.users import select_all_users, select_id

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


class Chats(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        state = dp.current_state(chat=message.from_user.id, user=message.from_user.id)

        state_str = str(await state.get_state())
        if state_str == "in_support":
            users = await select_all_users()
            users.remove(message.from_user.id)
            id = await select_id(message.from_user.id)
            for user in users:
                await bot.send_message(chat_id=user, text=f"#{id}")
                await message.send_copy(chat_id=user)

            raise CancelHandler()


def setup_chats(dp: Dispatcher):
    dp.middleware.setup(Chats())
