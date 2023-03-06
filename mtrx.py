from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from time import sleep
from datetime import datetime
from PIL import Image

updater = Updater(
    token="5594782594:AAERk4NH8Cubaj7DkWqRJohCokUP5V7FfLA", use_context=True)


def start(update: Update, context: CallbackContext):
    if update.message.chat_id == 5074618670:
        while True:
            if datetime.now().hour == int('15') and datetime.now().minute == int('10'):
                
                f = open('caption.txt', "r", encoding="utf-8")
                caption = f.read()

                im1 = Image.open('carbon.png')
                width, height = im1.size
                im2 = Image.open('wm.png')
                width1, height1 = im2.size
                back_im = im1.copy()
                back_im.paste(im2,  (width - width1 - 150, height - height1 - 150), im2)
                back_im.save('post.png', quality=95)

                keyboard = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text='Join The MTRX', url='t.me/mtrx_ir')]])
                
                context.bot.sendPhoto(
                    chat_id='@mtrx_ir',
                    photo=open('post.png', 'rb'),
                    caption=f'{caption}',
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN)

                f.close()
            sleep(60)
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,
                                text='با عرض پوزش شما مجاز به ارسال پست نمیباشید')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
