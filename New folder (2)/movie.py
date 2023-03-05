from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, ReplyKeyboardMarkup
from telegram.chataction import ChatAction
from bs4 import BeautifulSoup
import requests
import shutil
import re
import os
from time import sleep

updater = Updater(
    token="5214206611:AAFSmIBMqzRQiU6jdNefg4PbOP6VHYnLtIE", use_context=True)

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
userList = []
users = []
chatids = []

URL = "https://www.uptvs.com/%d9%81%db%8c%d9%84%d9%85-%d9%be%d9%84%d9%86%da%af-%d8%b3%db%8c%d8%a7%d9%87-2-black-panther-2-2022-%d8%a8%d8%a7-%d8%af%d9%88%d8%a8%d9%84%d9%87-%d9%81%d8%a7%d8%b1%d8%b3%db%8c.html"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

name = soup.find("h1", class_="text-white h2 pb-lg-1 pb-md-1").contents[0]
links = soup.find_all("a", class_="btn-green")
img = soup.find(
    "img", class_="top-single-img")['src'].replace('\n', '').replace(' ', '')
imdb = soup.find_all(
    "span", class_="font-weight-bold text-white small-15")[0].contents[0].replace(' ', '')
like = soup.find_all(
    "span", class_="font-weight-bold text-white small-15")[1].contents[0]
mp4 = soup.find('div', class_='row align-items-center').find('source')['src']
ganers = soup.find('span', class_='d-inline-block category_post').find_all('a')
country = soup.find(
    'span', class_='d-md-inline-block d-none').contents[0].replace('  ', '').replace('\n', '')
time = soup.find(
    'div', class_='col-md col-lg').contents[-1].replace('  ', '').replace('\n', '')
year = soup.find(
    'span', class_='d-inline-block mx-half text-white-25').next_sibling.replace('  ', '').replace('\n', '')
about = soup.find('p', class_='show-read-more').contents[0]
aboutt = about[about.find(':')+2:]

# for ganer in ganers[1:]:
#     print(ganer.contents[0].replace(' ', ''))
# print(ganers[1:][:].contents[:])

# from telegram.error import BadRequest
# def is_user_there(channel, chat_id) -> bool:
#     chat_member = context.bot.getChatMember(channel,update.message.chat_id) # this will return a ChatMember object
#     if chat_member.status in [‘administrator’, ‘creator’, ‘member’]:
#         return True
#     else:
#         return False

if len(links) > 5:
    link1 = links[0]['href']
    link2 = links[1]['href']
    link3 = links[2]['href']
    link4 = links[3]['href']
    link5 = links[4]['href']
    link6 = links[5]['href']
else:
    link1 = links[0]['href']
    link2 = links[1]['href']
    link3 = links[2]['href']

res = requests.get(img, stream=True)
with open('test.jpg', 'wb') as f:
    shutil.copyfileobj(res.raw, f)


def start(update: Update, context: CallbackContext):
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    global starts
    starts = ' '.join(str(x) for x in re.findall(r'\d+', update.message.text))

    if str(update.message.chat_id) == starts:
        context.bot.sendMessage(update.message.chat_id, text='{} {} عزیز، \n کلیک هایی که خود فرد بروی لینک اختصاصی خود میکند شمرده نمی شود، کلیک ها می‌بایست از طریق دیگر حساب های تلگرام صورت بگیرد'.format(
            update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''))
    else:
        userList.append(starts)
        users.append('@{}'.format(update.message.from_user.username))
        chatids.append(update.message.chat_id)

        keyboard = [
            ['مشاهده خدمات'],
            ['ارتباط با پشتیبانی', 'ورود به ناحیه کاربری'],
            ['دانلود اپلیکیشن', 'درباره نت سرویس'],
            ['مشاهده تخفیف ها']
        ]
        context.bot.send_message(chat_id=update.message.chat_id, text='<b>{} {}</b> عزیز\n از اینکه مارو انتخاب کردید سپاسگزاریم 🌸🌹 \n از طریق دکمه های زیر میتونید از امکانات این ربات استفاده فرمایید.'.format(
            update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True), parse_mode=ParseMode.HTML)
        context.bot.send_message(
            chat_id=5189755201, text='یک نفر با ایدی @{} ربات رو استارت کرد'.format(update.message.from_user.username))
        with open('ids.txt', 'a') as f:
            f.write('id:  {}    |    chatid:     {}\n\n____________________________________________________________________________________\n\n'.format(
                update.message.from_user.username, update.message.chat_id))

def main_keyboard(update: Update, context: CallbackContext):
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    if update.message.text == 'مشاهده نصب کنندگان':
        context.bot.sendMessage(
            update.message.chat_id, text='تعداد کل نصب کنندگان: {}'.format(len(users)))
        context.bot.sendMessage(update.message.chat_id, text='{}'.format(
            users).replace("', '", '\n').replace("['", ''). replace("']", ''))
    elif update.message.text == 'مشاهده خدمات':
        keyboard = [
            ['هاست و دامنه', 'خدمات وب‌سایت'],
            ['طراحی و گرافیک', 'دیجیتال مارکتینگ'],
            ['شبکه های مجازی', 'ثبتی و حقوقی'],
            ['بازگشت به منوی اصلی']
        ]
        context.bot.send_message(chat_id=update.message.chat_id, text='به فروشگاه نت سرویس خوش آمدید\nبا کلیک بروی هر خدمات ما میتوانید جزییات سرویس را مشاهده فرمایید.',
                                 reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True))
    elif update.message.text == 'مشاهده تخفیف ها':
        if userList.count(str(update.message.chat_id)) > 2:
            context.bot.sendMessage(
                update.message.chat_id, text='ربات با موفقیت برای شما فعال شد\n از این پس میتوانید از تمامی ابزار های ربات اسفتاده فرمایید')

        elif userList.count(str(update.message.chat_id)) == 2:
            context.bot.sendMessage(
                update.message.chat_id, text='تا کنون تعداد ۲ نفر با لینک شما به ربات پیوستنید فقط ۱ نفر دیگر باقیست')

        elif userList.count(str(update.message.chat_id)) == 1:
            context.bot.sendMessage(
                update.message.chat_id, text='تابحال فقط ی نفر با لینک شما به ربات پیوسته است')

        elif userList.count(str(update.message.chat_id)) == 0:
            context.bot.sendMessage(
                update.message.chat_id, text='برای اخذ کد تخفیف باید 3 نفر با لینک اختصاصی شما که در بنر زیر وجود دارند وارد ربات شوند\nبرای فعال سازی ربات بنر زیر را برای دوستان خودتون به اشتراک قرار دهید'.format(update.message.chat_id))
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(
                'mlogo.png', 'rb'), caption='<a href="http://t.me/netserviceshop_bot?start={}">نت سرویس | خدمات توسعه و رشد کسب و کار شما\n\nهاست و دامنه                  خدمات وب‌سایت\n\nطراحی و گرافیک             دیجیتال مارکتینگ\n\nشبکه های مجازی             ثبتی و حقوقی</a>'.format(update.message.chat_id), parse_mode=ParseMode.HTML)

    else:
        if update.message.chat.id == 5189755201:
            for chatid in chatids:
                context.bot.forward_message(chat_id='{}'.format(
                    chatid), from_chat_id=5189755201, message_id=update.message.message_id)
                context.bot.send_message(
                    chat_id=update.message.chat_id, text='پیام شما ارسال شد')
        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='پیام شما با موفقیت برای پشتیبانی ارسال گردید، \nدر اصرع وقت با شما ارتباط برقرارا خواهم کرد')
            context.bot.forward_message(
                chat_id='5189755201', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
            with open('Message.txt', 'a', encoding="utf-8") as z:
                z.write('آیدی:  {}    ||>>     {}\n\n____________________________________________________________________________________\n\n'.format(
                    update.message.from_user.username, update.message.text))

def unknown(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('دوبله فارسی', callback_data='persian')],
        [InlineKeyboardButton(text='1080p', url=f'{link1}'),
         InlineKeyboardButton(text='720p', url=f'{link2}'),
         InlineKeyboardButton(text='480p', url=f'{link3}')]
    ]
    if len(links) > 5:
        keyboard.append([InlineKeyboardButton(
            'زیرنویس فارسی', callback_data='original')])
        keyboard.append([InlineKeyboardButton(text='1080p', url=f'{link2}'),
                         InlineKeyboardButton(text='720p', url=f'{link3}'),
                         InlineKeyboardButton(text='480p', url=f'{link4}')])
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open('test.jpg', 'rb'), caption=f"""

{name}

‌امتیاز IMDB از 10:       {imdb}
محصول کشور:              {country}
سال ساخت:                  {year}
زمان:                            {time}

خلاصه داستان:
{aboutt}
""", reply_markup=InlineKeyboardMarkup(keyboard))


def button_handler(update: Update, context: CallbackContext):
    if update.callback_query.data == 'persian':
        update.callback_query.bot.answer_callback_query(
            update.callback_query.id, text='برای دانلود این فیلم با دوبله فارسی ابتدا فیلترشکن خود را خاموش بفرمایید سپس کیفیت دلخواه خود در پایین کلیک فرمایید', show_alert=True)

    elif update.callback_query.data == 'original':
        update.callback_query.bot.answer_callback_query(
            update.callback_query.id, text='برای دانلود این فیلم با زیرنویس فارسی ابتدا فیلترشکن خود را خاموش بفرمایید سپس کیفیت دلخواه خود در پایین کلیک فرمایید', show_alert=True)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, main_keyboard))
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
updater.start_polling()
updater.idle()
