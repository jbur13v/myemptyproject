import aiogram
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from var import *

token = ''
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welc(message: types.Message):
    await message.answer(start, reply_markup=menu)
# гл меню
@dp.message_handler(text='Конвертор валют')
async def convv(message: types.Message):
    await message.answer('Выберите валюту', reply_markup=currency_menu)
@dp.message_handler(text='Универ')
async def univ(message: types.Message):
    await message.answer('Что надо?', reply_markup=univmenu)
@dp.message_handler(text= 'Тут будет новая функция')
async def new(message: types.Message):
    await message.answer('Тут пока что пусто, тут будет новая функция в будущем', reply_markup=menu)
# Конверт
@dp.message_handler(text= '$')
async def univ(message: types.Message):
    await message.answer('Введите сумму')
@dp.message_handler()
async def text_message(msg: types.Message):
    c1 = int(msg.text) * usd
    if msg.text == 'Назад':
        await message.answer('', reply_markup=univmenu) 
    await bot.send_message(msg.from_user.id, f'$ {msg.text} ={c1} сум')

# @dp.message_handler(text= '€')
# async def univ(message: types.Message):
#     await message.answer('Введите сумму')
# @dp.message_handler()
# async def text_message(msg: types.Message):
#     c1 = int(msg.text) * euro
#     if msg.text == 'Назад':
#         await message.answer('', reply_markup=univmenu)
#     await bot.send_message(msg.from_user.id, f'€ {msg.text} ={c1} сум')

# @dp.message_handler(text= '₽')
# async def univ(message: types.Message):
#     await message.answer('Введите сумму')
# @dp.message_handler()
# async def text_message(msg: types.Message):
#     c1 = int(msg.text) * rubl
#     if msg.text == 'Назад':
#         await message.answer('', reply_markup=univmenu)
#     await bot.send_message(msg.from_user.id, f'₽ {msg.text} ={c1} сум')

#
@dp.message_handler(text='К началу')
async def idk(message: types.Message):
    await message.answer(start, reply_markup=menu)


@dp.message_handler(text = 'Рассписание звонков')
async def univ(message: types.Message):
    await message.answer('''1.   9:30 10:50 
2. 11:00 12:20
3. 12:30 13:50
4. 14:30 15:50''')


@dp.message_handler(text = 'Обратная связь')
async def univ(message: types.Message):
    await message.answer('Tg: @jasurburiev')

@dp.message_handler(text = 'Назад')
async def univ(message: types.Message):
    await message.answer(start, reply_markup=menu)

@dp.message_handler(text='Рассписание')
async def univ(message: types.Message):
    await message.answer('Выберите день', reply_markup=sub)


@dp.message_handler(text = 'Понедельник')
async def univ(message: types.Message):
    await message.answer('''1. ----
2. АС УВД
3. Безопасность полетов''')

@dp.message_handler(text = 'Вторник')
async def univ(message: types.Message):
    await message.answer('''1. БЖД 
2. ТРД
3. Правила радиотелефонной связи в гражданской авиации''')

@dp.message_handler(text = 'Среда')
async def univ(message: types.Message):
    await message.answer('''1. АС УВД
2. Спец. Тренажерная подготовка
3. Спец. Тренажерная подготовка''')

@dp.message_handler(text = 'Четверг')
async def univ(message: types.Message):
    await message.answer('''1. Воздушная навигация
2. Человеческий фактор в авиации
3. Спец. английкий язык''')

@dp.message_handler(text = 'Пятница')
async def univ(message: types.Message):
    await message.answer('''1. Стажировка 
2. Стажировка
3. Стажировка''')
@dp.message_handler(text = 'Суббота')
async def univ(message: types.Message):
    await message.answer('''1. Спец. английкий язык
2. Спец. Тренажерная подготовка
3. Спец. Тренажерная подготовка''')

@dp.message_handler(text = 'К началу')
async def univ(message: types.Message):
    await message.answer(start, reply_markup=menu)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
