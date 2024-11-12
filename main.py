# Задание в README

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()
storage = MemoryStorage()


@dp.message(Command('keyboard'))
async def cmd_dynamic(message: Message):
    keyboard = kb.get_dynamic_keyboard()
    await message.answer("Нажмите на кнопку ниже:", reply_markup=keyboard)

@dp.callback_query(F.data == "show_more")
async def show_more(call: CallbackQuery):
    keyboard = kb.get_options_keyboard()
    await call.message.edit_text("Выберите опцию:", reply_markup=keyboard)

@dp.callback_query(F.data == "option_1")
async def option_1(call: CallbackQuery):
    await call.message.answer("Вы выбрали Опцию 1")

@dp.callback_query(F.data == "option_2")
async def option_2(call: CallbackQuery):
    await call.message.answer("Вы выбрали Опцию 2")


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