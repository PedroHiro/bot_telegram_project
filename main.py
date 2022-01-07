from src.telegram_bot import telegramBot
from src.driveBot import driveBot

#bot = telegramBot()
#bot.start()

driveBot = driveBot()
print(driveBot.get_data())
