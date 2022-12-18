from aiogram import types, Bot, Dispatcher
import  markups as nav

reply_markup = nav.mainMenu

TOKEN = '5831723467:AAGOaPKEhftzRPd1ud0NxegZ49KmIfVVA-U'

bot = Bot(token=TOKEN)

dp= Dispatcher(bot)

@dp.message_handler(commands=['menu'])
async def command_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное Меню', reply_markup= nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):

    if message.text == '⬅️ Главное меню':
        await bot.send_message(message.from_user.id,'⬅️ Главное меню', reply_markup= nav.mainMenuMenu)

    elif message.text == '📈 Посмотреть рейтинг':
        await bot.send_message(message.from_user.id, 'Какой-то рейтинг')

    elif message.text == '♦️ Ввести код':
        await bot.send_message(message.from_user.id, 'QR код')

    elif message.text == '✉ Наши соцсети':
        await bot.send_message(message.from_user.id, '✉ Наши соцсети', reply_markup= nav.tests2Menu)

    elif message.text == '📨 Телеграмм':
        await bot.send_message(message.from_user.id, 'Телеграмм - https://t.me/stackers_team')

    elif message.text == '👥 Вконтакте':
        await bot.send_message(message.from_user.id, 'Вконтакте - https://vk.com/stackers.team')

    elif message.text == '📸 Инстаграмм':
        await bot.send_message(message.from_user.id, 'Инстаграмм - https://www.instagram.com/stackers.team/')

    elif message.text == '📝 Посмотреть активные тесты':
        await bot.send_message(message.from_user.id,'📝 Активные тесты', reply_markup= nav.testsMenu)

    elif message.text == '🎄 Новогодний хакатон':
        await bot.send_message(message.from_user.id,'🎄 Новогодний хакатон - какой-то тест №1')

    elif message.text == '🍲 Beautiful Soup':
        await bot.send_message(message.from_user.id,'🍲 Beautiful Soup - какой-то тест №2')

    else:
        await message.reply('Неизвестная команда')
