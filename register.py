from aiogram import Dispatcher

from handlers.chats import register_chats
from handlers.registration import register_registration
from middlewares.chats import setup_chats


def register(dp: Dispatcher):
    register_registration(dp)
    register_chats(dp)

def setup_middlewares(dp: Dispatcher):
    setup_chats(dp)