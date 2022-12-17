from aiogram import types, Bot, Dispatcher
import  markups as nav

reply_markup = nav.mainMenu

TOKEN = '5831723467:AAGOaPKEhftzRPd1ud0NxegZ49KmIfVVA-U'

bot = Bot(token=TOKEN)

dp= Dispatcher(bot)

@dp.message_handler()
async def bot_message(message: types.Message):

    if message.text == '⬅️ Главное меню':
        await bot.send_message(message.from_user.id,'⬅️ Главное меню', reply_markup= nav.mainMenuMenu)

    elif message.text == '📝 Посмотреть активные тесты':
        await bot.send_message(message.from_user.id,'📝 Активные тесты', reply_markup= nav.testsMenu)

    elif message.text == '📈 Посмотреть рейтинг':
        await bot.send_message(message.from_user.id, 'Какой-то рейтинг')

    elif message.text == '♦️ Ввести код':
        await bot.send_message(message.from_user.id, 'QR код')

    else:
        await message.reply('Неизвестная команда')
