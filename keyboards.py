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

def get_dynamic_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    return builder.as_markup()

def get_options_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
    builder.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
    return builder.as_markup()




