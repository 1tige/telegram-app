from flask import Flask, request
from pyrogram import Client, filters
from pyrogram.types import Message

# Инициализация Flask-приложения
app = Flask(__name__)

# Инициализация Telegram клиента
api_id = '22731254'  # замените на ваш API ID
api_hash = 'a9a0a228967bdbad740ddd75bb00cc1b'  # замените на ваш API Hash
bot_token = '6751864090:AAFTfjqeTMQzWsx_tu_VYhwas0OX7RwK2Xw'  # замените на ваш токен бота

bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Обработчик команды /start
@bot.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply("Привет! Я твой новый бот.")

# Роут для проверки работы веб-приложения
@app.route('/')
def home():
    return "Hello, this is my Telegram bot running on Flask!"

# Роут для приема обновлений от Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    bot.process_update(update)
    return "ok"

if __name__ == '__main__':
    # Запуск бота и веб-приложения
    bot.start()
    app.run(port=5000)
