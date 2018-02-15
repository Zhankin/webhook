import telebot
import os
from flask import Flask, request

bot = telebot.TeleBot('510800243:AAEsmyadUWf8h6VL4YV0HbjXtvuYVLRNpFQ')

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    print ('!!!!!!!!!!!!!!!!!!')
    bot.set_webhook(url="https://zhankin-test-1.herokuapp.com/510800243:AAEsmyadUWf8h6VL4YV0HbjXtvuYVLRNpFQ")
    print ('!!!!!!!!!!!!!!!!!!')
    return "!", 200

server.run(host="0.0.0.0", port=int(os.environ.get('PORT')))
server = Flask(__name__)
