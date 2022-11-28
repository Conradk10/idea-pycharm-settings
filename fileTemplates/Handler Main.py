from loader import dp
from aiogram import types

from game.types import Player


@dp.message_handler(commands=[''])
async def cmd_(message: types.Message, player: Player):
    text, kb = await get_main_text(player)
    await message.reply(text, reply_markup=kb)


async def get_main_text(player: Player):
    text = ''
    kb = types.InlineKeyboardMarkup()
    return text, kb
