import telebot
bot = telebot.TeleBot('6814979011:AAECrnn5PKspr8AElct_KWEh2aM-UNSXP9U')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '___Дорогой друг рад приветствовать тебя у себя в гостях, раз ты обратился ко мне значит  у тебя плохое настроение не так ли?___', parse_mode='Markdown')

@bot.message_handler(commands=['mood'])
def main(message):
    bot.send_message(message.chat.id, '_Как я знаю людям для поднятия настроения рекомендуется съесть что-нибудь сладкое_ \nТак что советую тебе подкрепиться', parse_mode='Markdown')

@bot.message_handler(commands=['first'])
def main(message):
    bot.send_message(message.chat.id, 'Ещё рекомендую тебе послушать музычку [Вот как вариант](https://www.youtube.com/watch?v=edsx_MOhVnk)', parse_mode='Markdown')

@bot.message_handler(commands=['more'])
def main(message):
    bot.send_message(message.chat.id, 'Ну и ещё напоследок своетую тебе посмотреть мой любимый мультик [Лови] (https://youtu.be/gtTPHqB4dHc?feature=shared)', parse_mode='Markdown')

bot.infinity_polling()