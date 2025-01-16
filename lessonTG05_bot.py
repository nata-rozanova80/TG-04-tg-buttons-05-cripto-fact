import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

CRYPTO_API_URL = 'https://api.coingecko.com/api/v3/simple/price'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('crypto'))
async def cmd_crypto(message: types.Message):
    price_info = get_crypto_price('bitcoin')  # Получаем котировку биткоина
    await message.answer(price_info)



@dp.message(Command('fact'))
async def cmd_fact(message: Message):
    fact = get_random_fact()
    await message.answer(fact)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать! Используйте команды:\n/crypto <валюта> - узнать котировку криптовалюты\n/fact - получить случайный факт")


def get_crypto_price(currency):
    response = requests.get(CRYPTO_API_URL, params={'ids': currency, 'vs_currencies': 'usd'})
    if response.status_code == 200:
        data = response.json()
        if currency in data:
            price = data[currency]['usd']
            return f"Котировка {currency.capitalize()}: ${price}"
        else:
            return "Криптовалюта не найдена."
    else:
        return "Не удалось получить котировку."

def get_random_fact():
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return "Не удалось получить факт."


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
