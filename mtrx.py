from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from time import sleep
from datetime import time
from PIL import Image
import pytz

updater = Updater(
    token="5594782594:AAERk4NH8Cubaj7DkWqRJohCokUP5V7FfLA", use_context=True)

a = 0

def start(update, context):
    global a
    if update.message.chat_id == 5074618670:
        if a == 0:
            a = 1
            context.job_queue.run_daily(post,time(hour=9, minute=17, tzinfo=pytz.timezone('Asia/Tehran')),days=(0, 1, 2, 3, 4, 5, 6),context=update.message.chat_id) 
            context.bot.sendMessage(chat_id=update.message.chat_id,text='The robot started')
        else:
            context.bot.sendMessage(chat_id=update.message.chat_id,text='The robot is running')

    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text='Hello World !')

def post(context):
    sleep(30)
    f = open('caption.txt', "r", encoding="utf-8")

    im1 = Image.open('carbon.png')
    width, height = im1.size
    im2 = Image.open('wm.png')
    width1, height1 = im2.size
    back_im = im1.copy()
    back_im.paste(im2,  (width - width1 - 150, height - height1 - 140), im2)
    back_im.save('post.png', quality=95)

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text='Join The MTRX', url='t.me/mtrx_ir')]])
    context.bot.sendPhoto(chat_id='@mtrx_ir',photo=open('post.png', 'rb'),caption=f'{f.read()}',reply_markup=keyboard,parse_mode=ParseMode.MARKDOWN)

    f.close()

def text(update, context):
    world = ['fuck', 'no']
    if update.message.text in world:
            context.bot.deleteMessage (message_id = update.message.message_id, chat_id = update.message.chat_id)

def photo(update, context):
    if update.message.chat_id == 5074618670:
        # context.bot.getFile(update.message.photo[-1].file_id).download('carbon.png')
        txt = open("caption.txt", "w", encoding="utf-8")
        txt.write(f'{update.message.caption}\n‍'.replace('~', '*').replace("'", '`'))
        txt.close()
        with open("carbon.png", 'wb') as f:
            context.bot.get_file(update.message.document).download(out=f)
        context.bot.sendMessage(chat_id=update.message.chat_id, text="download succesfull")

updater.dispatcher.add_handler(CommandHandler("start", start, pass_job_queue=True))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))
updater.dispatcher.add_handler(MessageHandler(Filters.document, photo))
updater.start_polling()
updater.idle()

