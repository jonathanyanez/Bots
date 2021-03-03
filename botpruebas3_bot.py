#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from chatterbot import ChatBot
bot = telebot.TeleBot("ID:TOKEN")


def bot_conversacional(message):
    chatbot = ChatBot("Ejemplo Bot", trainer="chatterbot.trainers.ChatterBotCorups")
    respuesta=chatbot.get_response(mensaje)
    print("BOT: "+str(respuesta))
    


#commands es una lista de strings que contiene los comandos a los que contestará el bot
#Recibimos y enviamos una respuesta al comando start y help
@bot.message_handler(commands=["help", "start"])
def enviar_mensaje(message):
    bot.reply_to(message, "mensaje con el  metodo enviar_mensaje")



#Eco de los mensajes que mandas al bot
@bot.message_handler(func=lambda message: True)
def mensaje(message):
    bot.reply_to(message, message.text)



bot.polling()
