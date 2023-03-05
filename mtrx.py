from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import os
import time
import datetime

updater = Updater(
    token="5594782594:AAERk4NH8Cubaj7DkWqRJohCokUP5V7FfLA", use_context=True)

f =  open('a.txt')
caption = f.read()

def start(update: Update, context: CallbackContext):
    if update.message.chat_id == 5074618670:
        while True:
            if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 00:
                keyboard = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text='عضویت در کانال MTRX', url='t.me/mtrx_ir')]])
                context.bot.sendPhoto(chat_id='@mtrx_ir', photo=open('carbon.png', 'rb'),
                                      caption=f'{caption}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
            time.sleep(60)

    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,
                                text='با عرض پوزش شما مجاز به ارسال پست نمیباشید')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()

# token='5594782594:AAERk4NH8Cubaj7DkWqRJohCokUP5V7FfLA'
# channel = '@mtrx_ir'
# text = 'dd'
# requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={channel}&text={text}')