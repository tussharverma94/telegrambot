import telebot
import time
from call_script import callpy
from dir import give_path
import webbrowser
from desktop import call_desktop
from server_bot import throw
import pickle

f = open("C://Users//tussh//PycharmProjects//telegrambot//cred.txt", 'r')
bot_token2 = f.readline()
f.close()

# bot_token2 = "1294296291:AAGvyWUjmh3xLe1zvZorrms5sv_Atv5DpeE"

bot = telebot.TeleBot(token=bot_token2)


@bot.message_handler(commands=['game'])
def send_welcome(message):
    bot.reply_to(message, "Game started sir")
    provide_path = give_path()
    path = provide_path.p_path()
    call_obj = callpy(path)
    call_obj.call_python_file()


@bot.message_handler(commands=['game2'])
def send_welcome(message):
    bot.reply_to(message, "Game started sir")
    th = throw(mssg="", game=1)
    th.initial_var()
    result = th.get_farther()
    if result:
        bot.reply_to(message, "Game started succesfully")
    else:
        bot.reply_to(message, "Sorry there was some server issue")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,
                 'commands: \n /hey_david for calling david\n/google_search as "/google_search word"\n/open_google\n/help\n/game\n/game2 for server run game\n/play for this type "/play filename" \nFurther will be added soon')


@bot.message_handler(commands=['open_google', 'Open_Google'])
def send_welcome(message):
    bot.reply_to(message, "Opening google sir")
    webbrowser.open("https://google.com")


@bot.message_handler(commands=['google_search'])
def send_welcome(message):
    plain_text = message.text
    plain_text = plain_text[len("google_search") + 1:]
    th = throw(mssg=plain_text, browser=1)
    th.initial_var()
    result = th.get_farther()
    if result:
        bot.reply_to(message, "Searching for {} on your desktop".format(plain_text))
    else:
        bot.reply_to(message, "Not able to connect to you desktop due to some unavoidable reason")
    # webbrowser.open("https://google.com")


@bot.message_handler(commands=['play'])
def send_welcome(message):
    plain_text = message.text
    plain_text = plain_text[len("play") + 1:]
    th = throw(mssg=plain_text, play_f=1)
    th.initial_var()
    result = th.get_farther()
    if result:
        bot.reply_to(message, f"Playing {plain_text} on you desktop")
    else:
        bot.reply_to(message, "Not able to play due to some reason")


@bot.message_handler(commands=['hey_david'])
def send_welcome(message):
    plain_text = message.text
    th = throw(mssg=plain_text, david=1)
    th.initial_var()
    result = th.get_farther()
    if result:
        bot.reply_to(message, "david is live on desktop")
    else:
        bot.reply_to(message, "There is some problem in connecting to david")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
