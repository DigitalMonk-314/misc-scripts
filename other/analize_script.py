from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated
BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer(text='Это команда /start')


@dp.message(Command(commands='start', prefix='|'))
async def process_command_start(message: Message):
    await message.answer(text='И это команда /start')


# Этот хэндлер будет срабатывать на блокировку бота пользователем
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f"Пользователь {event.from_user.id} заблокировал бота")

if __name__ == "__main__":
    dp.run_polling(bot)
