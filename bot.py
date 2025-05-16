import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في بوت تداول كربتو! سيتم قريبًا إضافة كل أدوات التحليل والذكاء الاصطناعي.")

bot.polling()
