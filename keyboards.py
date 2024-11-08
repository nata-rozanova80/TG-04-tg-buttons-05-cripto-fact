from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет!")],
   [KeyboardButton(text="Пока!")]
], resize_keyboard=True)


inline_keyboard_url = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://ria.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/home')],
   [InlineKeyboardButton(text="Видео", url='https://vk.com/video')]
])


dynamic_keyboard = ["Показать больше...", "Опция 1", "Опция 2"]

async def dynamic_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in dynamic_keyboard:
       keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
   return keyboard.adjust(2).as_markup()
