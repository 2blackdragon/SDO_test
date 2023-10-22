from vkbottle.bot import Bot, Message
from config import VK_TOKEN
bot = Bot(VK_TOKEN)

@bot.on.private_message(text="<msg>")
async def echo_answer(message: Message, msg):
    users_info = await bot.api.users.get(message.from_id)
    await bot.api.messages.send(peer_id=users_info[0].id, random_id=0, message="Привет Павел Дуров!")

if __name__ == "__main__":
    bot.run_forever()