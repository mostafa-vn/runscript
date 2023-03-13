# _*_ coding: utf-8 _*_
import os, pyqrcode, png, re, socket, dns.resolver, string, requests, wget, time, urllib.parse, whois, whmcspy, urllib3
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, Filters
from telegram.chataction import ChatAction
from builtwith import builtwith
from zipfile import ZipFile
from textblob import TextBlob
from PIL import Image, ImageFilter, ImageEnhance
from time import sleep
from datetime import time
import pytz

updater = Updater(
    token="5594782594:AAERk4NH8Cubaj7DkWqRJohCokUP5V7FfLA", use_context=True)

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

clients = {}
a = 0

def start(update, context):
    global a, starts
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    starts = ' '.join(str(x) for x in re.findall(r'\d+', update.message.text))
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

def urlwhois(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
    
            arg = update.message.text.replace('/whois ', '').replace('http://', '').replace('https://', '')
            domain = whois.query(arg)
            website = domain.__dict__
            context.bot.send_message(chat_id = update.message.chat_id, text = 'آدرس وب‌سایت: {} \n ثبت کننده: {} \n کشور ثبت کننده: {} \n تاریخ ایجاد: {} \n تاریخ انقضا: {} \n آخرین بروزرسانی: {} \n لیست Name Server ها: {}'.format(website['name'], website['registrar'], website['registrant_country'], website['creation_date'], website['expiration_date'], website['last_updated'], website['name_servers']))
   
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار هویز از این فرمت استفاده کنید: \n /whois example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def iptourl(update: Update, context: CallbackContext):
    print('ss')
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/iptourl ', '')
            url = socket.gethostbyaddr(arg)[0]
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(url))
 
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار تبدیل آیپی به آدرس وب‌سایت از این فرمت استفاده کنید: \n /iptourl WebsiteIp')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def qrcode(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            context.bot.send_chat_action(update.message.chat_id, ChatAction. UPLOAD_PHOTO)
            arg = update.message.text.replace('/qrcode ', '')
            url = pyqrcode.create(arg)
            url.svg('%s.svg'%update.message.chat_id, scale=8)
            url.eps('%s.eps'%update.message.chat_id, scale=2)
            url.png('%s.png'%update.message.chat_id, scale=8)
            context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.svg'.format(update.message.chat_id), 'rb'))
            context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.eps'.format(update.message.chat_id), 'rb'))
            context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.png'.format(update.message.chat_id), 'rb'))
            os.system('del {}.svg'.format(update.message.chat_id))
            os.system('del {}.eps'.format(update.message.chat_id))
            os.system('del {}.png'.format(update.message.chat_id))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار تبدیل متن یا لینک به بارکد از این فرمت استفاده کنید: \n /qrcode yout text or link')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def filesize(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/filesize ', '')
            info = requests.head(arg)
            lenght = info.headers['content-length']
            if len(lenght) < 4 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} بایت'.format(lenght))
            elif len(lenght) == 4 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} کیلوبایت'.format(lenght[0:1]))
            elif len(lenght) == 5 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} کیلوبایت'.format(lenght[0:2]))
            elif len(lenght) == 6 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} کیلوبایت'.format(lenght[0:3]))
            elif len(lenght) == 7 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} مگابایت'.format(lenght[0:1]))
            elif len(lenght) == 8 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} مگابایت'.format(lenght[0:2]))
            elif len(lenght) == 9 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} مگابایت'.format(lenght[0:3]))
            elif len(lenght) == 10 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} گیگ'.format(lenght[0:1]))
            elif len(lenght) == 11 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'حجم فایل: {} گیگ'.format(lenght[0:2]))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار یافتن حجم فایل از روی لینک از این فرمت استفاده کنید: \n /filesize https://dl.example.com/filename.format')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def source(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/source ', '')
            r = requests.get(arg)
            source = r.text
            with open('{}.html'.format(update.message.chat_id), 'w', encoding='utf-8') as f:
                f.write(source)
            context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.html'.format(update.message.chat_id), 'rb'))
            os.system('del {}.html'.format(update.message.chat_id))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار دانلود سورس وب‌سایت از این فرمت استفاده کنید: \n /source https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def screen(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/screen ', '')
            BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?'
            url = urllib.parse.quote_plus(arg)
            path = '{}.jpg'.format(update.message.chat_id)
            response = requests.get(BASE + url, stream=True)
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    for chunk in response:
                        file.write(chunk)
                context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.jpg'.format(update.message.chat_id), 'rb'))
                os.system('del {}.jpg'.format(update.message.chat_id))

                context.bot.send_message(chat_id = update.message.chat_id, text = 'لطفا لینک خود را بررسی کرده و دوباره تلاش کنید')
    
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار اسکرین شات از سایت از این فرمت استفاده کنید: \n /screen https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def webip(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/webip ', '')
            ip = socket.gethostbyname(arg)
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(ip))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار نمایش آیپی وب‌سایت از این فرمت استفاده کنید: \n /webip https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def hashing(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/hash ', '')
            hashed = hash(arg)
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(hashed))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار هش کردن متن از این فرمت استفاده کنید: \n /hash your text')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def dnss(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/dns ', '')
            for server in dns.resolver.query(arg,'NS'):
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(server.target))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار پیدا کردن dns های وب‌سایت از این فرمت استفاده کنید: \n /dns example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def password(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            characters = string.ascii_letters  + string.digits
            password =  ''.join(choice(characters) for x in range(randint(8, 16)))
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(password))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار ساخت پسورد قوی تصادفی از این فرمت استفاده کنید: \n /password')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def passlist(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            f = []
            a = context.args[0]
            b = context.args[1]
            c = context.args[2]
            f.append(a)
            f.append(b)
            f.append(c)
            with open('passlist-{}.txt'.format(update.message.chat_id), 'w') as fa:
                for i in range(0,3):
                    for j in range(0,3):
                        for k in range(0,3):
                            for l in range(0,3):
                                fa.write('{}{}{}{}\n'.format(f[i], f[j], f[k], f[l]))
            context.bot.send_document(chat_id = update.message.chat_id, document = open('passlist-{}.txt'.format(update.message.chat_id), 'rb'))
            os.system('del passlist-{}.txt'.format(update.message.chat_id))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار ساخت پسوردلیست هدفمند از این فرمت استفاده کنید: \n /passlist number number number \n به جای number از کلمه یا عدد دلخواه خود استفاده کنید')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def translate(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/translate ', '')
            text = TextBlob(u'{}'.format(arg))
            if arg[1] in letter :
                translated = text.translate(to='fa')
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(translated))
            else:
                translated = text.translate(to='en')
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(translated))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار مترجم فارسی به انگلیسی و برعکس از این فرمت استفاده کنید: \n /translate your text')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def download(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/download ', '')
            lenght = requests.head(arg).headers['content-length']
            if len(lenght) > 8 :
                context.bot.send_message(chat_id = update.message.chat_id, text = 'به دلیل کنترل ترافیک سرور حداکثر حجم فایل برای دانلود ده مگابایت است')
            else:
                remote_url = arg
                reverced = remote_url[::-1]
                find = reverced.find('.')
                format = reverced[:reverced.find('.')][::-1]
                local_file = '{}.{}'.format(update.message.chat_id, format)
                wget.download(remote_url, local_file)
                context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.{}'.format(update.message.chat_id, format), 'rb'))
                os.system('del {}.{}'.format(update.message.chat_id, format))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار مدیریت دانلود از این فرمت استفاده کنید: \n /download https://dl.example.com/file.zip')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def myinfo(update: Update, context: CallbackContext):
    print('ss')
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            user = update.message.from_user
            file_id = context.bot.get_user_profile_photos(update.message.chat_id, 0).photos[0][-1].file_id
            context.bot.send_photo(chat_id = update.message.chat_id, photo = file_id, caption = 'نام: {} \n نام خانوادگی:{} \n شناسه کاربری: {} \n چت آیدی: {}'.format(user['first_name'], user['last_name'], user['username'], user['id']).replace('None', 'وجود ندارد'))


            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار  نمایش تمام اطلاعات  شما از این فرمت استفاده کنید: \n /myinfo')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def webtech(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:

            arg = update.message.text.replace('/webtech ', '')
            tech = builtwith(arg)
            for i in tech:
                b = tech['%s'%i]
                c = '{} is {}'.format(i, b)
                context.bot.send_message(chat_id = update.message.chat_id, text = '%s'%c)

            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار نمایش تکنولوژی ها بکررفته در وب‌سایت از این فرمت استفاده کنید: \n /screen https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def effect(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار قرار دادن افکت بروی عکس یا تبدیل عکس به استیکر عکس خود را برای ما ارسال فرمایید')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def effects(update: Update, context: CallbackContext):
    print('ff')
    if context.bot.getChatMember(chat_id = '@mtrx_ir', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
            context.bot.send_chat_action(update.message.chat_id, ChatAction.UPLOAD_PHOTO)
            context.bot.getFile(update.message.photo[-1]).download('{}.jpg'.format(update.message.chat_id))
            img = Image.open('{}.jpg'.format(update.message.chat_id))
            img.convert('L').save('{}-grayed.jpg'.format(update.message.chat_id))
            ImageEnhance.Color(img).enhance(3).save('{}-enhanced-color.jpg'.format(update.message.chat_id))
            ImageEnhance.Contrast(img).enhance(3).save('{}-enhanced-contrast.jpg'.format(update.message.chat_id))
            ImageEnhance.Brightness(img).enhance(3).save('{}-enhanced-brightness.jpg'.format(update.message.chat_id))
            img.filter(ImageFilter.BLUR).save("{}-blured.jpg".format(update.message.chat_id))
            img.filter(ImageFilter.CONTOUR).save("{}-CONTOUR.jpg".format(update.message.chat_id))
            img.filter(ImageFilter.EDGE_ENHANCE_MORE).save("{}-EDGE_ENHANCE_MORE.jpg".format(update.message.chat_id))
            img.save('{}-format.webp'.format(update.message.chat_id))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-grayed.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-enhanced-color.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-enhanced-contrast.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-enhanced-brightness.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-blured.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-CONTOUR.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('{}-EDGE_ENHANCE_MORE.jpg'.format(update.message.chat_id), 'rb'))
            context.bot.sendSticker(chat_id = update.message.chat_id, sticker = open('{}-format.webp'.format(update.message.chat_id), "rb"))
            os.system('del {}.jpg'.format(update.message.chat_id))
            os.system('del {}-grayed.jpg'.format(update.message.chat_id))
            os.system('del {}-enhanced-color.jpg'.format(update.message.chat_id))
            os.system('del {}-enhanced-contrast.jpg'.format(update.message.chat_id))
            os.system('del {}-enhanced-brightness.jpg'.format(update.message.chat_id))
            os.system('del {}-blured.jpg'.format(update.message.chat_id))
            os.system('del {}-CONTOUR.jpg'.format(update.message.chat_id))
            os.system('del {}-EDGE_ENHANCE_MORE.jpg'.format(update.message.chat_id))
            os.system('del {}-format.webp'.format(update.message.chat_id))

            context.bot.send_message(chat_id = update.message.chat_id, text = 'در تبدیل عکس شما به استیکر یه خطایی به وجود آمد که لاگ آن برای مدیریت ارسال شد، از شما پوزش می طلبیم')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/mtrx_ir')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))

updater.dispatcher.add_handler(CommandHandler("start", start, pass_job_queue=True))
updater.dispatcher.add_handler(CommandHandler('whois', urlwhois, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('iptourl', iptourl, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('qrcode', qrcode, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('filesize', filesize, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('source', source, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('screen', screen, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('webip', webip, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('hash', hashing, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('dns', dnss, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('password', password, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('passlist', passlist, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('translate', translate, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('download', download, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('myinfo', myinfo))
updater.dispatcher.add_handler(CommandHandler('webtech', webtech, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('effect', effect))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))
updater.dispatcher.add_handler(MessageHandler(Filters.document, photo))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, effects))

updater.start_polling()
updater.idle()

