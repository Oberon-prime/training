from aiogram import Bot, types
from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
import json
from pickcha.foto_id import *
import asyncio

from config import dp, bot

@dp.message_handler(Command("start"))
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id , "Привет {}".format(message.from_user.first_name))
    await bot.send_message(message.from_user.id, "ЗДесь ты найдешь тренировочные программы на разные группы мышц ."
                                                 "Хорошей Трени")
@dp.message_handler(Command("help"))
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id , "Привет {}".format(message.from_user.first_name))
    await bot.send_message(message.from_user.id, "Можешь воспользоваться командами для получения комплексов упражнений \n"+
                           "/kom1 \n"+ "             /kom2 \n"+ "/kom3 \n" + "             /kom4 \n"+ "/kom5 \n"+
                           "             /kom6")

@dp.message_handler(commands=['legs'])
async def process_legs_command(message: types.Message):
    await bot.send_message(message.from_user.id , "Привет! это тренинг на ноги и бедра " )
    for i in range(6):

        f_name = [foto0,foto1,foto2,foto3,foto4,foto5]
        cap_name = ["вот фото 0","vot1","ввот фото 2","djn 3","vot4","vot 5"]
        await bot.send_photo(chat_id=message.from_user.id,
                         photo=f_name[i],
                         caption=cap_name[i])
        await asyncio.sleep(2)

@dp.message_handler(commands=['arms'])
async def process_arms_command(message: types.Message):
    album = types.MediaGroup()

    # Прикрепляем фото и видео
    photo_file_id = "AgACAgIAAxkBAAIKDWAw7qYzSU6s5zhnaehkjPW9io7FAAI3sjEbDueISZPAIXyrF8PgDD_Rmi4AAwEAAwIAA20AA_BQAgABHgQ"
    '''photo_url = "https://i.pinimg.com/originals/13/25/68/132568dbe8f3316aa56551dba527e7f7.jpg"
    photo_bytes = InputFile("photos/cat.jpg")'''
    video_file_id = "BAACAgIAAxkBAAIKXWAxLGQumodw9exdML6JqFRpm5TJAALQDgACDueISYGAWbDXYpnNHgQ"
    photo_bytes = "AgACAgIAAxkBAAIKA2Aw7lIwpLbn1HrfT0eAmcblZAK6AAImsjEbDueISVkUG7STreoKZBnKly4AAwEAAwIAA20AA84cBwABHgQ"
    photo_url = "AgACAgIAAxkBAAIJ_mAw7itplNwt6GnAy9aV2EDxmvktAAIWsjEbDueISVnTzXFFo8yjHPLAly4AAwEAAwIAA20AA2IhBwABHgQ"
    album.attach_photo(
        photo=photo_file_id,
        caption="красота")
    album.attach_photo(photo=photo_url)
    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id,
                       caption="Видео ")
    await message.answer_media_group(media=album)


@dp.message_handler(commands=['kom1'])
async def process_kom1_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(8):

        cap_name = ["видос 1.1", "видос1.2", "видос1.3", "видос1.4", "видос1.5", "видос1.6","видос1.7","видос1.8"]
        await bot.send_video(chat_id=message.from_user.id,
                             video=kom1[i],
                             caption=cap_name[i])
        await asyncio.sleep(4)
    await bot.send_message(message.from_user.id, "Хорошей Тренировки")

@dp.message_handler(commands=['kom2'])
async def process_kom2_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(7):
        cap_name = ["видос 2.1", "видос2.2", "видос2.3", "видос2.4", "видос2.5", "видос2.6", "видос2.7"]
        await bot.send_video(chat_id=message.from_user.id,
                             video=kom2[i],
                             caption=cap_name[i])
        await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, "Хорошей Тренировки")

@dp.message_handler(commands=['kom3'])
async def process_kom3_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(8):
        cap_name = ["видос 3.1", "видос3.2", "видос3.3", "видос3.4", "видос3.5", "видос3.6", "видос3.7","видос3.8"]
        await bot.send_video(chat_id=message.from_user.id,
                             video=kom3[i],
                             caption=cap_name[i])
        await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, "Хорошей Тренировки")

@dp.message_handler(commands=['kom4'])
async def process_kom4_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(7):
        cap_name = ["видос 4.1", "видос4.2", "видос4.3", "видос4.4", "видос4.5", "видос4.6", "видос4.7", "видос4.8"]
        await bot.send_video(chat_id=message.from_user.id,
                             video=kom4[i],
                             caption=cap_name[i])
        await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, "Хорошей Тренировки")

@dp.message_handler(commands=['kom5'])
async def process_kom5_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(7):
        cap_name = ["видос 5.1", "видос5.2", "видос5.3", "видос5.4", "видос5.5", "видос5.6", "видос5.7", "видос5.8"]
        await bot.send_video(chat_id=message.from_user.id,
                             video=kom5[i],
                             caption=cap_name[i])
        await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, "Хорошей Тренировки")

@dp.message_handler(commands=['kom6'])
async def process_kom6_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! это тренинг на ноги и бедра ")
    for i in range(7):
        cap_name = ["видос 6.1", "видос6.2", "видос6.3", "видос6.4", "видос6.5", "видос6.6", "видос6.7", "видос6.8"]
        await bot.send_video(chat_id=message.from_user.id,
                                 video=kom6[i],
                                 caption=cap_name[i])
        await asyncio.sleep(3)

    await bot.send_message(message.from_user.id,"Хорошей Тренировки")
print("вот")



if __name__ == '__main__':
    executor.start_polling(dp)