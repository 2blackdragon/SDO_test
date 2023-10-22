import aio_pika, json
from tg_bot.main import bot
import asyncio

async def recieve_from_queue(): 
     connection = await aio_pika.connect_robust( 
         host="localhost" 
     ) 
     queue_name = "data_to_send" 
     async with connection: 
         channel = await connection.channel() 

         await channel.set_qos(prefetch_count=10) 
         queue = await channel.declare_queue(queue_name) 

         async with queue.iterator() as queue_iter: 
             async for message in queue_iter: 
                 async with message.process(): 
                     order_id = message.body.decode()
                    
                     await router(order_id)

async def router(order_id):
    data = json.loads(order_id)
    print(data["tg_id"], data["text"])
    # await send_from_queue(data["tg_id"], data["text"])
    match data["social_media"]:
        case "tg":
            await send_to_tg(data)
        case "vk":
            await send_to_vk(data)
        


async def send_to_tg(data):
    await bot.send_message(data["tg_id"], data["text"])

async def send_to_vk(data):
    ...



asyncio.run(recieve_from_queue())
