import aiogram
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

start = 'Выберите категрию'

convert = KeyboardButton('Конвертор валют')
rasp = KeyboardButton('Универ')
newfunc = KeyboardButton('Тут будет новая функция')

menu = ReplyKeyboardMarkup(resize_keyboard=True).add(convert).add(rasp).add(newfunc)

usdollar = KeyboardButton('$')
euro = KeyboardButton('€')
rubl = KeyboardButton('₽')
back = KeyboardButton('Назад')

currency_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(usdollar).add(euro).add(rubl).add(back)

usd = 11395.00
eu = 12027.31
rub = 149.27

#Main menu buttons
ras = KeyboardButton('Рассписание')
tm = KeyboardButton('Рассписание звонков')
contact = KeyboardButton('Обратная связь')
back = KeyboardButton('Назад')
univmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(ras).add(tm).add(contact).add(back)


#Questions or phrases
mn = KeyboardButton('Понедельник')
tu = KeyboardButton('Вторник')
wed = KeyboardButton('Среда')
thr = KeyboardButton('Четверг')
fri = KeyboardButton('Пятница')
sat = KeyboardButton('Суббота')
tomenu = KeyboardButton('К началу')
sub = ReplyKeyboardMarkup(resize_keyboard=True).add(mn).add(tu).add(wed).add(thr).add(fri).add(sat).add(tomenu)