from aiogram import Bot, types
from aiogram.utils import executor
from aiogram import types
import json
from config import dp, bot

# Высылка фото(видео) в бот для  дальнейшего получения ID .длявидеоизменитьимяфайлаиsend
@dp.message_handler(commands=['get_id'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! жди загрузки файла" )
    await bot.send_video(message.from_user.id, open("vid7.9.mp4", "rb"))


# ОТправление полученного фото (получит его ID)
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)
    jsonData = str(message)
    dictData = json.loads(jsonData)
    print(dictData["photo"][0]["file_id"])

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)
    jsonData = str(message)
    dictData = json.loads(jsonData)
    print(dictData["video"]["file_id"])

if __name__ == '__main__':
    executor.start_polling(dp)
