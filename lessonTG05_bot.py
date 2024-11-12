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


#dp = Dispatcher(bot)


# @dp.message(Command('crypto'))
# async def cmd_crypto(message: types.Message):
#     currencies = message.text.split()[1:]  # Получаем все валюты после команды
#     if currencies:
#         prices = []
#         for currency in currencies:
#             price_info = get_crypto_price(currency.lower())
#             prices.append(price_info)
#         await message.answer("\n".join(prices))  # Отправляем все котировки в одном сообщении
#     else:
#         await message.answer(
#             "Пожалуйста, укажите валюту:\n"
#             "1. Bitcoin - `bitcoin`\n"
#             "2. Ethereum - `ethereum`\n"
#             "3. Ripple - `ripple`\n"
#             "4. Litecoin - `litecoin`\n"
#             "5. Bitcoin Cash - `bitcoin-cash`\n"
#             "6. Cardano - `cardano`\n"
#             "7. Polkadot - `polkadot`\n"
#             "8. Dogecoin - `dogecoin`\n"
#             "9. Chainlink - `chainlink`\n"
#             "10. Binance Coin - `binancecoin`\n"
#             "11. Solana - `solana`\n"
#             "12. Tron - `tron`\n"
#             "13. Stellar - `stellar`\n"
#             "14. Tether - `tether`\n"
#             "15. USD Coin - `usd-coin`."
#         )

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