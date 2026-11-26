from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Токен бота
BOT_TOKEN = '8258671649:AAF7EN2LPiHITbozJl0a6M6Rt2W47veA51k'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Список с ID администраторов бота
admin_ids: list[int] = [8370079324]

# Фильтр для админов
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

# Фильтр для чисел в сообщении
class NumberInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        return False

# Хэндлер для сообщений с числами
@dp.message(F.text.lower().startswith('найди числа'), NumberInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Нашел: {", ".join(str(num) for num in numbers)}'
    )

# Хэндлер для сообщений с "найди числа", но без чисел
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')

# Хэндлер для админов
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')

# Хэндлер для всех остальных
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)

