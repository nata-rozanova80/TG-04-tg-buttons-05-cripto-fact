
# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока".
# При нажатии на кнопку "Привет" бот должен отвечать "Привет, {имя пользователя}!",
# а при нажатии на кнопку "Пока" бот должен отвечать "До свидания, {имя пользователя}!".

import asyncio

from aiogram import Bot, Dispatcher, F

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
import keyboards as kb



bot = Bot(token=TOKEN)
dp = Dispatcher()
storage = MemoryStorage()



@dp.message(Command('buttons'))
async def buttons(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_url)


@dp.message(F.text == "Привет!")
async def button_hi(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)

@dp.message(F.text == "Пока!")
async def button_bye(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}', reply_markup=kb.main)

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Привет!' , reply_markup=kb.main)

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())