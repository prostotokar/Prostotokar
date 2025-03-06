import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Завантажуємо змінні оточення з файлу .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Клавіатура
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("📅 Записатися"))

# Обробник команди /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привіт! Чим можу допомогти?", reply_markup=menu_keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
