
import os
import telebot
from flask import Flask, request

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Olá, eu sou o Zion, o assistente oficial do projeto ZETTA!")

@bot.message_handler(commands=['tokenomics'])
def tokenomics(message):
    bot.reply_to(message, "📊 Tokenomics ZETTA: 60% Liquidez, 15% Marketing, 10% Time, 10% Desenvolvimento, 5% Reserva.")

@bot.message_handler(commands=['pre_venda'])
def pre_venda(message):
    bot.reply_to(message, "🚀 A pré-venda ocorrerá via Gempad com auditoria e KYC. Preço inicial: $0.005.")

@bot.message_handler(commands=['whitepaper'])
def whitepaper(message):
    bot.reply_to(message, "📄 Whitepaper ZETTA: https://zettaword.com/whitepaper")

@app.route("/" + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@app.route("/")
def webhook():
    return "Zion está rodando."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
