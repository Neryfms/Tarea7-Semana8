
import time
import telebot
from telebot import types

TOKEN = '1942066480:AAH9-9DD7EP3_ofEMOkfoDAd7wAg9A16w-s'

knownUsers = [] 
userStep = {} 

commands = {  
    'start'       : 'Iniciar bot',
    'help'        : 'Ayuda'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect.add('Celsius a Fahrenheit', 'Fahrenheit a Celsius', 'Celsius a Kelvin', 'Fahrenheit a Kelvin', 'Kelvin a Celsius', 'Kelvin a Fahrenheit')

hideBoard = types.ReplyKeyboardRemove()  

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuario detectadp pero uso otro comando y no \"/start\"")
        return 0



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Solo estos comandos estan disponibles\n\n"
    for key in commands: 
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text) 

@bot.message_handler(commands=['start'])
def command_image(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Hey, ¡hola!")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Mira, ahorita no te puedo atender")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Estoy ocupado atendiendo a otros usuarios")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Te atenderé cuando termine con ellos")
    time.sleep(10)
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Jajajaja")
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    bot.send_message(cid, "¿En serio creiste que estoy ocupado atendiendo a otros usuarios?")
    time.sleep(3)
    bot.send_sticker (cid, 'CAACAgIAAxkBAAPxYQticDcCYpnWiVG4kEfOsS_8ORAAAiQDAAK1cdoGn4orPORRz70gBA')
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Bueno, basta de bromas")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Será un gusto ayudarte")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Te ayudare a gestionar las formulas de conversion de temperatura")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Por favor elije una opcion\nY te mostraré su formula", reply_markup=imageSelect) 
    userStep[cid] = 1  


@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    bot.send_chat_action(cid, 'typing')

    if text == 'Celsius a Fahrenheit':  
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Celsius a Fahrenheit")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('C a f.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    elif text == 'Fahrenheit a Celsius':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Fahrenheit a Celsius")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('f a c.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    elif text == 'Celsius a Kelvin':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Celsius a Kelvin")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('C a k.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    elif text == 'Fahrenheit a Kelvin':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Fahrenheit a Kelvin")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('f a k.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    elif text == 'Kelvin a Celsius':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Kelvin a Celsius")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('k a c.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    elif text == 'Kelvin a Fahrenheit':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Has seleccionado opcion: \nFormula de Kelvin a Fahrenheit")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la formula")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAMkYQtQZtK3nOUUGrCkIW4xEN_8cVkAAlcAA8GcYAzGAv2zVJumNCAE')
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(5)   
        bot.send_photo(cid, open('k a f.png', 'rb'),
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa /start para realzar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Pero, ten paciencia")
        bot.send_sticker (cid, 'CAACAgEAAxkBAAOBYQtYSxzDC9NKzJqBnyl0Pd6N3DcAAu0BAAI4DoIRPCeAbIAXmgMgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Saludos!")
        
        userStep[cid] = 0  
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡Y no!")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAOVYQtbCrBAdATWpwAB7Y4_kdcRotywAAJpAAPBnGAMTjMSb1IRHIwgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Tienes que usar el teclado predefinido!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Por favor, intentalo de nuevo.")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBOWELZSQEmu4xqPpTgnQv4lxM0Oo1AAK6AANSiZEjLQ0Qg2F3qk0gBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Cuidadito")




@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):

    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡Y no!")
    bot.send_sticker (m.chat.id, 'CAACAgIAAxkBAAOVYQtbCrBAdATWpwAB7Y4_kdcRotywAAJpAAPBnGAMTjMSb1IRHIwgBA')
    bot.send_message(m.chat.id, "Yo no entiendo la palabra \"" + m.text + "\"\nUsa /start para usar el bot")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¡Qué esto no se vuelva a repetir!")
    bot.send_sticker (m.chat.id,'CAACAgIAAxkBAAPdYQthbfLBJlfwsYFoFgsH6_ykG3UAAoQAA0QNzxdaythEmzlA7iAE')
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¿Entendido?")



bot.polling()