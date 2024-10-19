import telebot
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7876224683:AAH5nzlDO6R4Wn9ZsYMq16tu0REkq3C_a7s")
@bot.message_handler(commands=['start', 'hello','Старт', 'Привет'])
def send_welcome(message):
        bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()