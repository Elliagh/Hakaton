from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')
btnCreateQR = KeyboardButton("♦️ Создать код")
btnSendMes = KeyboardButton("Отправить уведомление")
btnUploadFile = KeyboardButton("Загрузить тест")

# btnUploadFile
btnCSVFile = KeyboardButton('Загрузить CSV файл')
CSVFile = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCSVFile, btnMain)

# Main Menu
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCreateQR, btnSendMes, btnUploadFile)
