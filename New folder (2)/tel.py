from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

updater = Updater(
    token="897679934:AAFvcYB6o5FKrJFvSse0GpM7YizBc44g17M", use_context=True)

def unknown(update: Update, context: CallbackContext):
    if update.message.chat_id == 234064838:
        context.bot.sendPhoto(chat_id='@seventestq', photo=open('bsh.jpg', 'rb'), caption=(update.message.text).replace('$', '`'), reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='هاست وردپرس آلمان', url='https://7ho.st/hosting/wordpress/germany'),
            InlineKeyboardButton(text='هاست وردپرس ایران', url='https://7ho.st/hosting/wordpress/iran')],
            [InlineKeyboardButton(text='انجمن سون هاست', url='https://7ho.st/hosting/wordpress/germany'),
            InlineKeyboardButton(text='بانک مقالات', url='https://7ho.st/hosting/wordpress/iran')],
            [InlineKeyboardButton(text='ثبت دامنه', url='https://t.me/whois7bot')],
        ]), parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id, text='با عرض پوزش شما مجاز به ارسال پست نمیباشید')

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.start_polling()
updater.idle()