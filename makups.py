from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')

# Main Menu
btnTest = KeyboardButton('📝 Посмотреть активные тесты')
btnTop = KeyboardButton('📈 Посмотреть рейтинг')
btnCode = KeyboardButton('/includeKey')
btnInfo = KeyboardButton('✉ Наши соцсети')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTest, btnTop, btnCode, btnInfo)

# Tests
btnFirst = KeyboardButton('🎄 Новогодний хакатон')
btnSecond = KeyboardButton('🍲 Beautiful Soup')
testsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFirst, btnSecond, btnMain)
