import telebot

API_TOKEN = '8170595803:AAGl2sBlbqb4tBKBakhZ7Aib2jvnVlo72so'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чем могу помочь")


@bot.message_handler(func=lambda message: message.text is not None)
def handle_messages(message):
    text = message.text.lower()

    if "здравствуйте" or "здраствуйте"  or "здравтвуйте" or "дравствуйте" in text:
        bot.reply_to(message, "Здравствуйте! Добро пожаловать в Startup House! 🚀")
    elif "ии" in text or "бизнес" in text:
        bot.reply_to(message, "Интересная тема! Расскажи, как ты используешь ИИ в бизнесе? 💡")
    elif "salom" in text or "бизнес" in text:
        bot.reply_to(message, "Salom! Startup Housega xush kelibsiz🚀")
    elif "привет" in text or "бизнес" in text:
        bot.reply_to(message, "Привет! Добро пожаловать в Startup House! 🚀")
    else:
        bot.reply_to(message, "Простите я вас не понимаю😭")


bot.infinity_polling()
