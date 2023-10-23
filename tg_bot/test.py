import config
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=config.BOT_TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения


# Хэндлер на команду /test1
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.reply("Hello!")
    print(message.from_user.id, message.from_user.first_name)
    await send_from_queue(770746159, 'hi')

async def send_from_queue(tg_id, text):
    await bot.send_message(tg_id, text)

def main():
    print("Started")
    executor.start_polling(dp, skip_updates=True)



if __name__ == "__main__":
    # Запуск бота
    main()