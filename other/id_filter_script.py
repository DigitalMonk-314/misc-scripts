from aiogram import Bot, Dispatcher
from aiogram.types import Message
BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def show_id(message: Message):
    print("Ваш ID:", message.from_user.id)
    await message.answer(f"Ваш ID: {message.from_user.id}")

if __name__ == "__main__":
    dp.run_polling(bot)