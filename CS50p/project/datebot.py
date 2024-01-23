import telebot
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime
from project import days_until_today,convert_jalali,convert_Gregorian

bot = telebot.TeleBot("6447204395:AAG9nj5T5C5ABCAlXh285hMbL4o9eVx0dqQ")

@bot.message_handler(commands=['start'])
def main(message):
    butt = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    butt.add("Jalali to Gregorian" , "Gregorian to Jalali" , "contact with me")
    bot.reply_to(message, "Hi \nHow can I help you?",reply_markup = butt)

@bot.message_handler(func=lambda m: m.text == "contact with me")
def info(message):
    button1 = telebot.types.InlineKeyboardButton("Ali", url= "Https://t.me/ali_ensa")
    button2 = telebot.types.InlineKeyboardButton("Mahdi", url= "Https://t.me/mahdii_aii")
    markup = telebot.types.InlineKeyboardMarkup(row_width = 2)
    markup.add(button1, button2)
    bot.reply_to(message, "It was a team work", reply_markup = markup)

@bot.message_handler(func=lambda m: m.text == "Jalali to Gregorian")
def Jalali(message):
    jalal = bot.send_message(message.chat.id, "Enter Persian (Jalali) Date\n(in the format of yyyy/mm/dd) :")
    bot.register_next_step_handler(jalal, jalali_input)

def jalali_input(message):
    a = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    b = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30]
    try:
        year, month, day = map(int, message.text.split("/"))
    except:
        bot.send_message(message.chat.id, "Invalid input. Please try again ")
    if year >= 0:
        x = (year + 1) % 4
        if ((not x == 0) and 0 < month <= 12 and 0 < day <= a[month - 1]) or (x == 0 and 0 < month <= 12 and 0 < day <= b[month - 1]):
            year1, month1, day1 = map(int, convert_jalali(year, month, day).split("/"))
            date = datetime.datetime(year1, month1, day1).strftime("%B/%d/%Y")
            bot.send_message(message.chat.id, f"convert : {date} \n\nTime interval until now : {days_until_today(year1, month1, day1)}")
        else:
            bot.send_message(message.chat.id, "Invalid input. Please try again ")
    else:
        bot.send_message(message.chat.id, "Invalid input. Please try again ")

@bot.message_handler(func=lambda m: m.text == "Gregorian to Jalali")
def Gregorian(message):
    Gregorian = bot.send_message(message.chat.id, "Enter Gregorian Date\n(in the format of mm/dd/yyyy) :")
    bot.register_next_step_handler(Gregorian, Gregorian_input)


def Gregorian_input(message):
    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        month, day, year = map(int, message.text.split("/"))
    except:
        bot.send_message(message.chat.id, "Invalid input. Please try again ")

    if year > 0:
        x = year % 4
        if ((not x == 0) and 0 < month <= 12 and 0 < day <= a[month - 1]) or (x == 0 and 0 < month <= 12 and 0 < day <= b[month - 1]):
            bot.send_message(message.chat.id, f"convert : {convert_Gregorian(year,month,day)} \n\nTime interval until now : {days_until_today(year, month, day)}")
        else:
            bot.send_message(message.chat.id, "Invalid input. Please try again ")
    else:
        bot.send_message(message.chat.id, "Invalid input. Please try again ")

@bot.message_handler()
def onather(message):
    bot.reply_to(message, "How can I help you?")

bot.infinity_polling()
