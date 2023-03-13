# _*_ coding: utf-8 _*_
import os, pyqrcode, png, re, socket, dns.resolver, string, requests, wget, time, urllib.parse, whois, whmcspy, urllib3
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram.chataction import ChatAction
from builtwith import builtwith
from zipfile import ZipFile
from textblob import TextBlob
from PIL import Image, ImageFilter, ImageEnhance

updater = Updater(token='5263618429:AAGIaGeMg4OAOzSDFGGYCDWdIJibuICKpLI', use_context=True)
whmcs = whmcspy.WHMCS('https://me.netservice.shop/includes/api.php', 'utJh3yzMa1iLxaPoq9oE8YyVh5Dq40UC', 'DGejdF2j4gy0GgYccKniwdBdbksLlNyO')
urllib3.disable_warnings()

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
userList = []
users = []
chatids = []
clients = {}
clientsdetails = {}

def start(update: Update, context: CallbackContext):
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    global starts, clientsid
    starts = ' '.join(str(x) for x in re.findall(r'\d+', update.message.text))
    if len(starts) == 9:
        clientsid = int('%s'%(starts[4:6]))
        clients.update({update.message.chat_id:clientsid})
        clientsdetails.update({update.message.chat_id:{'products':{'active':{}, 'inactive':{}}, 'domains':{'active':{}, 'inactive':{}}, 'tickets':{'open':{}, 'closed':{}}}})
        keyboard = [
            ['ناحیه کاربری'],
            ['دانلود اپلیکیشن', 'دریافت کد تخفیف'],
            ['درباره نت سرویس', 'ارتباط با پشتیبانی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = '<b>{} {}</b> عزیز\n از اینکه مارو انتخاب کردید سپاسگزاریم 🌸🌹 \n از طریق دکمه های زیر میتونید از امکانات این ربات استفاده فرمایید.'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True), parse_mode = ParseMode.HTML)
    elif str(update.message.chat_id) == starts:
        context.bot.sendMessage(update.message.chat_id, text='{} {} عزیز، \n کلیک هایی که خود فرد بروی لینک اختصاصی خود میکند شمرده نمی شود، کلیک ها می‌بایست از طریق دیگر حساب های تلگرام صورت بگیرد'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''))
    else:
        userList.append(starts)
        users.append('@{}'.format(update.message.from_user.username))
        chatids.append(update.message.chat_id)

        keyboard = [
            ['ناحیه کاربری'],
            ['دانلود اپلیکیشن', 'دریافت کد تخفیف'],
            ['درباره نت سرویس', 'ارتباط با پشتیبانی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = '<b>{} {}</b> عزیز\n از اینکه مارو انتخاب کردید سپاسگزاریم 🌸🌹 \n از طریق دکمه های زیر میتونید از امکانات این ربات استفاده فرمایید.'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True), parse_mode = ParseMode.HTML)
        context.bot.send_message(chat_id = 5189755201, text = 'یک نفر با ایدی @{} ربات رو استارت کرد'.format(update.message.from_user.username))
        with open('ids.txt', 'a') as f:
            f.write( 'id:  {}    |    chatid:     {}\n\n____________________________________________________________________________________\n\n'.format(update.message.from_user.username, update.message.chat_id))

def urlwhois(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/whois ', '').replace('http://', '').replace('https://', '')
            domain = whois.query(arg)
            website = domain.__dict__
            context.bot.send_message(chat_id = update.message.chat_id, text = 'آدرس وب‌سایت: {} \n ثبت کننده: {} \n کشور ثبت کننده: {} \n تاریخ ایجاد: {} \n تاریخ انقضا: {} \n آخرین بروزرسانی: {} \n لیست Name Server ها: {}'.format(website['name'], website['registrar'], website['registrant_country'], website['creation_date'], website['expiration_date'], website['last_updated'], website['name_servers']))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار هویز از این فرمت استفاده کنید: \n /whois example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def iptourl(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/iptourl ', '')
            url = socket.gethostbyaddr(arg)[0]
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(url))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار تبدیل آیپی به آدرس وب‌سایت از این فرمت استفاده کنید: \n /iptourl WebsiteIp')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def qrcode(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار تبدیل متن یا لینک به بارکد از این فرمت استفاده کنید: \n /qrcode yout text or link')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def filesize(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار یافتن حجم فایل از روی لینک از این فرمت استفاده کنید: \n /filesize https://dl.example.com/filename.format')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def source(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/source ', '')
            r = requests.get(arg)
            source = r.text
            with open('{}.html'.format(update.message.chat_id), 'w', encoding='utf-8') as f:
                f.write(source)
            context.bot.send_document(chat_id = update.message.chat_id, document = open('{}.html'.format(update.message.chat_id), 'rb'))
            os.system('del {}.html'.format(update.message.chat_id))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار دانلود سورس وب‌سایت از این فرمت استفاده کنید: \n /source https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def screen(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
            else:
                context.bot.send_message(chat_id = update.message.chat_id, text = 'لطفا لینک خود را بررسی کرده و دوباره تلاش کنید')
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار اسکرین شات از سایت از این فرمت استفاده کنید: \n /screen https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def webip(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/webip ', '')
            ip = socket.gethostbyname(arg)
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(ip))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار نمایش آیپی وب‌سایت از این فرمت استفاده کنید: \n /webip https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def hashing(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/hash ', '')
            hashed = hash(arg)
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(hashed))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار هش کردن متن از این فرمت استفاده کنید: \n /hash your text')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def dnss(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/dns ', '')
            for server in dns.resolver.query(arg,'NS'):
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(server.target))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار پیدا کردن dns های وب‌سایت از این فرمت استفاده کنید: \n /dns example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def password(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            characters = string.ascii_letters  + string.digits
            password =  ''.join(choice(characters) for x in range(randint(8, 16)))
            context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(password))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار ساخت پسورد قوی تصادفی از این فرمت استفاده کنید: \n /password')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def passlist(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار ساخت پسوردلیست هدفمند از این فرمت استفاده کنید: \n /passlist number number number \n به جای number از کلمه یا عدد دلخواه خود استفاده کنید')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def translate(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/translate ', '')
            text = TextBlob(u'{}'.format(arg))
            if arg[1] in letter :
                translated = text.translate(to='fa')
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(translated))
            else:
                translated = text.translate(to='en')
                context.bot.send_message(chat_id = update.message.chat_id, text = '{}'.format(translated))
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار مترجم فارسی به انگلیسی و برعکس از این فرمت استفاده کنید: \n /translate your text')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def download(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار مدیریت دانلود از این فرمت استفاده کنید: \n /download https://dl.example.com/file.zip')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def myinfo(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            user = update.message.from_user
            file_id = context.bot.get_user_profile_photos(update.message.chat_id, 0).photos[0][-1].file_id
            context.bot.send_photo(chat_id = update.message.chat_id, photo = file_id, caption = 'نام: {} \n نام خانوادگی:{} \n شناسه کاربری: {} \n چت آیدی: {}'.format(user['first_name'], user['last_name'], user['username'], user['id']).replace('None', 'وجود ندارد'))

        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار  نمایش تمام اطلاعات  شما از این فرمت استفاده کنید: \n /myinfo')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def webtech(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
            arg = update.message.text.replace('/webtech ', '')
            tech = builtwith(arg)
            for i in tech:
                b = tech['%s'%i]
                c = '{} is {}'.format(i, b)
                context.bot.send_message(chat_id = update.message.chat_id, text = '%s'%c)
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار نمایش تکنولوژی ها بکررفته در وب‌سایت از این فرمت استفاده کنید: \n /screen https://example.com')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def effect(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای استفاده از ابزار قرار دادن افکت بروی عکس یا تبدیل عکس به استیکر عکس خود را برای ما ارسال فرمایید')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))
def effects(update: Update, context: CallbackContext):
    if context.bot.getChatMember(chat_id = '@netserviceshop', user_id = update.message.chat_id).status[0] in ['m', 'a', 'c']:
        try:
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
        except:
            context.bot.send_message(chat_id = update.message.chat_id, text = 'در تبدیل عکس شما به استیکر یه خطایی به وجود آمد که لاگ آن برای مدیریت ارسال شد، از شما پوزش می طلبیم')
    else:
        keyboard = [
            [InlineKeyboardButton('عضویت در کانال', 'https://t.me/netserviceshop')]
            ]
        context.bot.sendMessage(update.message.chat_id, text='برای استفاده از امکانات این ربات می‌بایست در کانال رسمی نت سرویس در تلگرام عضو شوید', reply_markup =  InlineKeyboardMarkup(keyboard))

def contacts(update: Update, context: CallbackContext):
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    keyboard = [
    ['ارسال تیکت پشتیبانی'],
    ['ارتباط مستقیم با پشتیبانی', 'تماس تلفنی با نت سرویس'],
    ['بازگشت به منوی اصلی']
    ]
    context.bot.send_message(chat_id = update.message.chat_id, text = 'کاربر گرامی شماره همراه شما با موفقیت برای ما ارسال گردید،\n در اصرع وقت با شما تماس خواهیم گرفت.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    context.bot.forward_message(chat_id='5189755201', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main_keyboard(update: Update, context: CallbackContext):
    global clientsid
    context.bot.send_chat_action(update.message.chat_id, ChatAction.TYPING)
    if update.message.text == 'مشاهده نصب کنندگان':
        context.bot.sendMessage(update.message.chat_id, text='تعداد کل نصب کنندگان: {}'.format(len(users)))
        context.bot.sendMessage(update.message.chat_id, text='{}'.format(users).replace("', '", '\n').replace("['", ''). replace("']", ''))
    elif update.message.text == 'ناحیه کاربری':
        if update.message.chat_id in clients:
            keyboard = [
                ['دامنه ها', 'سرویس ها'],
                ['پشتیبانی', 'مالی'],
                ['خروج از ناحیه کاربری']
                ]
            context.bot.send_message(chat_id = update.message.chat_id, text = 'شما با موفقیت به ناحیه کاربری خود وارد شده اید\n\nاز طریق دکمه های زیر میتوانید اقدام به مدیریت ناحیه کاربری خود کنید', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
        else:
            keyboard = [
                [InlineKeyboardButton('اطلاعات بیشتر', 'https://t.me/netserviceshop/2')]
                ]
            context.bot.send_message(chat_id = update.message.chat_id, text = 'برای اتصال حساب کاربریتان به ربات تلگرام می‌بایست کد اتصال خود را از ناحیه کاربری نت سرویس کپی کرده و برای ربات ارسال کنید.', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'سرویس ها':
        keyboard = [
            ['ثبت سفارش جدید', 'سرویس های من'],
            ['بازگشت']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'کاربر عزیز شما به بخش سرویس ها وارد شده اید،\nابتدا دکمه موردنظر خود را از دکمه های زیر انتخاب کرده تا به صفحه ی بعد هدایت شوید.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'دامنه ها':
        keyboard = [
            ['دامنه های من'],
            ['تمدید دامنه', 'ثبت دامنه جدید'],
            ['بازگشت']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'کاربر عزیز شما به بخش دامنه ها وارد شده اید،\nابتدا دکمه موردنظر خود را از دکمه های زیر انتخاب کرده تا به صفحه ی بعد هدایت شوید.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'پشتیبانی':
        keyboard = [
            ['ارسال تیکت جدید', 'تیکت ها'],
            ['بازگشت']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش پشتیبانی خوش آمدید،\nقصد انجام چه فعالیتی دارید؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'مالی':
        keyboard = [
            ['کیف پول', 'صورتحساب ها'],
            ['بازگشت']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش مدیریت مالی و حسابداری نت سرویس خوش آمدید\nابتدای دکمه ای که قصد انجام آن فرایند را دارید را انتخاب کنید', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'بازگشت':
        keyboard = [
            ['دامنه ها', 'سرویس ها'],
            ['پشتیبانی', 'مالی'],
            ['خروج از ناحیه کاربری']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'با موفقیت به صفحه اصلی مدیریت ناحیه کاربری خود بازگشتید\nقصد انجام چه فرایندی را دارید؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    elif update.message.text == 'دامنه های من':
        for domains in whmcs.get_clients_domains(clientid=clientsid, active=True):
            clientsdetails[update.message.chat_id]['domains']['active'][domains['domainname']] = domains['expirydate']
        for domains in whmcs.get_clients_domains(clientid=clientsid, active=False):
            clientsdetails[update.message.chat_id]['domains']['inactive'][domains['domainname']] = domains['expirydate']

        count = len(clientsdetails[update.message.chat_id]['domains']['active']) + len(clientsdetails[update.message.chat_id]['domains']['inactive'])
        if count == 0:

            context.bot.send_message(text = '{}{} عزیز،\n❕هیچ دامنه ای در ناحیه کاربری شما یافت نشد\nبرای ثبت دامنه میتوانید از دکمه ثبت دامنه جدید استفاده نمایید.'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), chat_id = update.message.chat_id)
        else:
            keyboard = []
            for i in clientsdetails[update.message.chat_id]['domains']['active']:
                keyboard.append([InlineKeyboardButton('%s (فعال)'%(list(clientsdetails[update.message.chat_id]['domains']['active'].items())[::-1][0][0]), 'https://me.netservice.shop/clientarea.php?action=domains')])
                count = count-1
            for i in clientsdetails[update.message.chat_id]['domains']['inactive']:
                keyboard.append([InlineKeyboardButton('%s (غیرفعال)'%(list(clientsdetails[update.message.chat_id]['domains']['active'].items())[::-1][0][0]), 'https://me.netservice.shop/clientarea.php?action=domains')])
                count = count-1
            context.bot.send_message(text = 'تمام دامنه های موجود در ناحیه کاربریتان در پایین لیست شده اند و با کلیک بروی هر دامنه به قسمت پیکربندی دامنه هدایت میشوید', chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'سرویس های من':
        for products in whmcs.get_clients_products(clientid=clientsid, active=True):
            clientsdetails[update.message.chat_id]['products']['active'][products['ordernumber']] = products['name']
        for products in whmcs.get_clients_products(clientid=clientsid, active=False):
            clientsdetails[update.message.chat_id]['products']['inactive'][products['ordernumber']] = products['name']

        count = len(clientsdetails[update.message.chat_id]['products']['active']) + len(clientsdetails[update.message.chat_id]['products']['inactive'])

        if count == 0:
            context.bot.send_message(text = '{}{} عزیز،\n❕هیچ سرویس فعالی در ناحیه کاربری شما یافت نشد'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), chat_id = update.message.chat_id)
        else:
            keyboard = [
                [InlineKeyboardButton('سرویس های فعال من', callback_data = 'active_products')],
                [InlineKeyboardButton('سرویس های معلق من', callback_data = 'inactive_products')]
                ]
            context.bot.send_message(chat_id = update.message.chat_id, text = 'لطفا وضعیت سرویس های را جهت نمایش انتخاب فرمایید', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'تیکت ها':
        for tickets in whmcs.get_tickets(clientid=clientsid, status="Open"):
            clientsdetails[update.message.chat_id]['tickets']['open'][tickets['tid']] = tickets['subject']
        for tickets in whmcs.get_tickets(clientid=clientsid, status="Closed"):
            clientsdetails[update.message.chat_id]['tickets']['closed'][tickets['tid']] = tickets['subject']

        count = len(clientsdetails[update.message.chat_id]['tickets']['open']) + len(clientsdetails[update.message.chat_id]['tickets']['closed'])
        if count == 0:
            context.bot.send_message(text = '{}{} عزیز،\n❕شما تاکنون هیچ تیکت پشتیبانی ایجاد نکرده اید'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), chat_id = update.message.chat_id)
        else:
            keyboard = []
            for i in clientsdetails[update.message.chat_id]['tickets']['open']:
                keyboard.append([InlineKeyboardButton('%s (باز)'%clientsdetails[update.message.chat_id]['tickets']['open'][i], 'https://me.netservice.shop/supporttickets.php')])
                count = count-1
            for i in clientsdetails[update.message.chat_id]['tickets']['closed']:
                keyboard.append([InlineKeyboardButton('%s (بسته)'%clientsdetails[update.message.chat_id]['tickets']['closed'][i], 'https://me.netservice.shop/supporttickets.php')])
                count = count-1
            context.bot.send_message(text = 'تمامی تیکت های شما در زیر لیست شده اند\nشما میتواند با کلیک بروی تیکت موردنظرتان جزییات بیشتر تیکت را مشاهده فرمایید', chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'صورتحساب ها':
        keyboard =[
        [InlineKeyboardButton('مشاهده صورتحساب ها', 'https://me.netservice.shop/clientarea.php?action=invoices')]
        ]
        context.bot.send_message(text = 'برای مشاهده یا پرداخت صورتحساب هایتان از طریق دکمه مشاهده صورتحساب ها میتوانید اقدام فرمایید', chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'کیف پول':
        keyboard =[
        [InlineKeyboardButton('مدیریت کیف پول', 'https://me.netservice.shop/clientarea.php?action=addfunds')]
        ]
        context.bot.send_message(text = 'برای مدیریت موجودی کیف پول نت سرویس خود می توانید از طریق دکمه مدیریت کیف پول اقدام فرمایید', chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'تمدید دامنه':
        keyboard =[
        [InlineKeyboardButton('تمدید دامنه', 'https://me.netservice.shop/cart/domain/renew')]
        ]
        context.bot.send_message(text = 'برای تمدید دامنه های خود می توانید از طریق دکمه تمدید دامنه اقدام فرمایید' , chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ثبت دامنه جدید':
        context.bot.send_message(text = 'برای جستجوی دامنه موردنظر یا بررسی آزاد بودن دامنه، دامنه موردنظر خود را ارسال کنید\n\n ❕ مثال: example.com \n' , chat_id = update.message.chat_id)

    elif update.message.text == 'ارسال تیکت جدید':
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای ایجاد تیکت پشتیبانی و ارتباط با نت سرویس فقط کافیست پیام خود را برای ما ارسال فرمایید\n\n❕متن پیام می بایست به زبان فارسی باشد')

    elif update.message.text == 'ثبت سفارش جدید':
        keyboard = [
            ['هاست و دامنه', 'خدمات وب‌سایت'],
            ['طراحی و گرافیک', 'دیجیتال مارکتینگ'],
            ['شبکه های مجازی', 'ثبتی و حقوقی'],
            ['بازگشت']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به فروشگاه نت سرویس خوش آمدید\nبا کلیک بروی هر خدمات ما میتوانید جزییات سرویس را مشاهده فرمایید.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'ارتباط با پشتیبانی':
        keyboard = [
            ['ارسال تیکت پشتیبانی'],
            ['ارتباط مستقیم با پشتیبانی', 'تماس تلفنی با نت سرویس'],
            ['بازگشت به منوی اصلی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'لطفا یکی از دکمه ها را انتخاب کنید', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    elif update.message.text == 'دانلود اپلیکیشن':
        keyboard = [
        [InlineKeyboardButton('دانلود از کافه بازار', 'https://cafebazaar.ir/app/shop.netservice.me')],
        [InlineKeyboardButton('دانلود از مایکت', 'https://myket.ir/app/shop.netservice.me')],
        [InlineKeyboardButton('دانلود با لینک مستقیم', 'https://netservice.shop/netservice.apk')]
        ]
        context.bot.send_document(chat_id = update.message.chat_id, document = open('maslan_apk.zip', 'rb'), reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'درباره نت سرویس':
        keyboard = [
            [InlineKeyboardButton('دقیق ارقام پیشرو', callback_data = 'aboutus')],
            [InlineKeyboardButton('مشاهده مجوز ها', callback_data = 'badge')],
            [InlineKeyboardButton('نت سرویس در رسانه ها', callback_data = 'channels')]
            ]
        context.bot.send_location(chat_id = update.message.chat_id, latitude = '37.276282', longitude = '49.587425')
        context.bot.send_message(chat_id = update.message.chat_id, text = 'لطفا دکمه موردنظر خود را انتخاب فرمایید', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'دریافت کد تخفیف':
        if userList.count(str(update.message.chat_id)) > 2:
            context.bot.sendMessage(update.message.chat_id, text='ربات با موفقیت برای شما فعال شد\n از این پس میتوانید از تمامی ابزار های ربات اسفتاده فرمایید')

        elif userList.count(str(update.message.chat_id)) == 2:
            context.bot.sendMessage(update.message.chat_id, text='تا کنون تعداد ۲ نفر با لینک شما به ربات پیوستنید فقط ۱ نفر دیگر باقیست')

        elif userList.count(str(update.message.chat_id)) == 1:
            context.bot.sendMessage(update.message.chat_id, text='تابحال فقط ی نفر با لینک شما به ربات پیوسته است')

        elif userList.count(str(update.message.chat_id)) == 0:
            context.bot.sendMessage(update.message.chat_id, text='برای اخذ کد تخفیف باید 3 نفر با لینک اختصاصی شما که در بنر زیر وجود دارند وارد ربات شوند\nبرای فعال سازی ربات بنر زیر را برای دوستان خودتون به اشتراک قرار دهید'.format(update.message.chat_id))
            context.bot.send_photo(chat_id = update.message.chat_id, photo = open('mlogo.png', 'rb'), caption = '<a href="http://t.me/netserviceshop_bot?start={}">نت سرویس | خدمات توسعه و رشد کسب و کار شما\n\nهاست و دامنه                  خدمات وب‌سایت\n\nطراحی و گرافیک             دیجیتال مارکتینگ\n\nشبکه های مجازی             ثبتی و حقوقی</a>'.format(update.message.chat_id), parse_mode = ParseMode.HTML)

    elif update.message.text == 'خروج از ناحیه کاربری':
        keyboard = [
            ['ناحیه کاربری'],
            ['دانلود اپلیکیشن', 'دریافت کد تخفیف'],
            ['درباره نت سرویس', 'ارتباط با پشتیبانی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به منوی اصلی بازگشتید \n لطفا برای ادامه یکی از دکمه هارا انتخاب فرمایید.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'بازگشت به منوی اصلی':
        keyboard = [
            ['ناحیه کاربری'],
            ['دانلود اپلیکیشن', 'دریافت کد تخفیف'],
            ['درباره نت سرویس', 'ارتباط با پشتیبانی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به منوی اصلی بازگشتید \n لطفا برای ادامه یکی از دکمه هارا انتخاب فرمایید.', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'بازگشت به عقب':
        keyboard = [
            ['هاست و دامنه', 'خدمات وب‌سایت'],
            ['طراحی و گرافیک', 'دیجیتال مارکتینگ'],
            ['شبکه های مجازی', 'ثبتی و حقوقی'],
            ['بازگشت به منوی اصلی']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به فروشگاه اصلی برگشتید\nاز طریق دکمه ها میتوانید به خدمات موردنیاز خود دسترسی پیدا کنید', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    elif update.message.text == 'هاست و دامنه':
        keyboard = [
        ['ثبت دامنه', 'نمایندگی ثبت دامنه'],
        ['هاست NVMe SSD', 'هاست وردپرس'],
        ['هاست پایتون', 'نمایندگی هاست'],
        ['بازگشت به عقب']
        ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش هاست و دامنه خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'خدمات وب‌سایت':
        keyboard = [
        ['ساخت وب‌سایت', 'بهینه سازی و سئو'],
        ['گواهینامه SSL', 'وب-اپلیکیشن'],
        ['اخذ نمادهای اعتماد', 'خرید لایسنس'],
        ['بازگشت به عقب']
        ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش خدمات وب‌سایت خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'طراحی و گرافیک':
        keyboard = [
            ['طراحی وب‌سایت', 'طراحی اپلیکیشن'],
            ['طراحی لوگو', 'طراحی بنر'],
            ['لوگوموشن', 'موشن گرافیک'],
            ['بازگشت به عقب']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش طراحی و گرافیک خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'دیجیتال مارکتینگ':
        keyboard = [
            ['پیامک انبوه', 'تبلیغات گوکل'],
            ['ایمیل مارکتینگ', 'ریپورتاژ آگهی'],
            ['تبلیغات پاپ آپ', 'بک لینک'],
            ['مشاوره رایگان', 'تولید محتوا'],
            ['بازگشت به عقب']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش دیجیتال مارکتینگ خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'شبکه های مجازی':
        keyboard = [
            ['ربات اینستاگرام', 'دیگر خدمات اینستاگرام'],
            ['ربات تلگرام', 'دیگر خدمات تلگرام'],
            ['شماره مجازی', 'پروکسی تلگرام'],
            ['بازگشت به عقب']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش خدمات شبکه های مجازی خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))
    elif update.message.text == 'ثبتی و حقوقی':
        keyboard = [
            ['ثبت شرکت', 'ثبت برند'],
            ['گواهینامه ISO', 'کارت بازرگانی'],
            ['روزنامه رسمی', 'اخذ پروانه کسب'],
            ['بازگشت به عقب']
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'به بخش خدمات ثبتی و حقوقی خوش آمدید\nکدام بخش مورد نیاز شما می‌باشد؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    elif update.message.text == 'ثبت دامنه':
        keyboard = [
        [InlineKeyboardButton('ثبت دامنه', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'نمایندگی ثبت دامنه':
        keyboard = [
        [InlineKeyboardButton('نمایندگی ثبت دامنه', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'هاست NVMe SSD':
        keyboard = [
        [InlineKeyboardButton('هاست NVMe SSD', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'هاست وردپرس':
        keyboard = [
        [InlineKeyboardButton('هاست وردپرس', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'هاست پایتون':
        keyboard = [
        [InlineKeyboardButton('هاست پایتون', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'نمایندگی هاست':
        keyboard = [
        [InlineKeyboardButton('نمایندگی هاست', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'ساخت وب‌سایت':
        keyboard = [
        [InlineKeyboardButton('ساخت وب‌سایت', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'بهینه سازی و سئو':
        keyboard = [
        [InlineKeyboardButton('بهینه سازی و سئو', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'گواهینامه SSL':
        keyboard = [
        [InlineKeyboardButton('گواهینامه SSL', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'وب-اپلیکیشن':
        keyboard = [
        [InlineKeyboardButton('وب-اپلیکیشن', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'اخذ نمادهای اعتماد':
        keyboard = [
        [InlineKeyboardButton('اخذ نمادهای اعتماد', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'خرید لایسنس':
        keyboard = [
        [InlineKeyboardButton('خرید لایسنس', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'طراحی وب‌سایت':
        keyboard = [
        [InlineKeyboardButton('طراحی وب‌سایت', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'طراحی اپلیکیشن':
        keyboard = [
        [InlineKeyboardButton('طراحی اپلیکیشن', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'طراحی لوگو':
        keyboard = [
        [InlineKeyboardButton('طراحی لوگو', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'طراحی بنر':
        keyboard = [
        [InlineKeyboardButton('طراحی بنر', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'لوگوموشن':
        keyboard = [
        [InlineKeyboardButton('لوگوموشن', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'موشن گرافیک':
        keyboard = [
        [InlineKeyboardButton('موشن گرافیک', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'پیامک انبوه':
        keyboard = [
        [InlineKeyboardButton('پیامک انبوه', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'تبلیغات گوکل':
        keyboard = [
        [InlineKeyboardButton('تبلیغات گوکل', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ایمیل مارکتینگ':
        keyboard = [
        [InlineKeyboardButton('ایمیل مارکتینگ', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ریپورتاژ آگهی':
        keyboard = [
        [InlineKeyboardButton('ریپورتاژ آگهی', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'تبلیغات پاپ آپ':
        keyboard = [
        [InlineKeyboardButton('تبلیغات پاپ آپ', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'بک لینک':
        keyboard = [
        [InlineKeyboardButton('بک لینک', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'مشاوره رایگان':
        keyboard = [
        [InlineKeyboardButton('مشاوره رایگان', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'تولید محتوا':
        keyboard = [
        [InlineKeyboardButton('تولید محتوا', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'ربات اینستاگرام':
        keyboard = [
        [InlineKeyboardButton('ربات اینستاگرام', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'دیگر خدمات اینستاگرام':
        keyboard = [
        [InlineKeyboardButton('دیگر خدمات اینستاگرام', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ربات تلگرام':
        keyboard = [
        [InlineKeyboardButton('ربات تلگرام', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'دیگر خدمات تلگرام':
        keyboard = [
        [InlineKeyboardButton('دیگر خدمات تلگرام', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'شماره مجازی':
        keyboard = [
        [InlineKeyboardButton('شماره مجازی', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'پروکسی تلگرام':
        keyboard = [
        [InlineKeyboardButton('پروکسی تلگرام', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'ثبت شرکت':
        keyboard = [
        [InlineKeyboardButton('ثبت شرکت', 'https://netservice.shop/')]
        ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ثبت برند':
        keyboard = [
        [InlineKeyboardButton('ثبت برند', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'گواهینامه ISO':
        keyboard = [
        [InlineKeyboardButton('گواهینامه ISO', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'کارت بازرگانی':
        keyboard = [
        [InlineKeyboardButton('کارت بازرگانی', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'روزنامه رسمی':
        keyboard = [
        [InlineKeyboardButton('روزنامه رسمی', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'اخذ پروانه کسب':
        keyboard = [
        [InlineKeyboardButton('اخذ پروانه کسب', 'https://netservice.shop/')]
            ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'برای مشاهده جزییات، پلن ها و ثبت سفارش بروی دکمه بالا کلیک فرمایید ', reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.message.text == 'ارسال تیکت پشتیبانی':
        keyboard = [
        [InlineKeyboardButton('پرسش و پاسخ', 'https://me.netservice.shop/submitticket.php?step=2&deptid=3'),
        InlineKeyboardButton('مالی و فروش', 'https://me.netservice.shop/submitticket.php?step=2&deptid=2')],
        [InlineKeyboardButton('پشتیبانی فنی', 'https://me.netservice.shop/submitticket.php?step=2&deptid=4'),
        InlineKeyboardButton('هاست ودامنه', 'https://me.netservice.shop/submitticket.php?step=2&deptid=5')]
        ]
        context.bot.sendMessage(update.message.chat_id, 'لطفا دپارتمان موردنظر را جهت پشتیبانی انتخاب نمایید', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'ارتباط مستقیم با پشتیبانی':
        keyboard = [
        [InlineKeyboardButton('پشتیبانی نت سرویس', 'https://t.me/netservice_support')]
        ]
        context.bot.send_message(chat_id = update.message.chat_id, text = 'اگر ریپورت هستید و قادر به پیام دادن به پشتیبان تلگرام نمی‌باشید پیام خود را همینجا برای ما ارسال کنید تا ما با شما ارتباط برقرار کنیم', reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.message.text == 'تماس تلفنی با نت سرویس':
        keyboard = [
            [KeyboardButton(text = 'ارسال شماره همراه من', request_contact=True)],
            ['ارسال تیکت پشتیبانی'],
            ['ارتباط مستقیم با پشتیبانی', 'تماس تلفنی با نت سرویس'],
            ['بازگشت به منوی اصلی']
            ]
        context.bot.send_contact(chat_id = update.message.chat_id, phone_number = '+982128421124', first_name = 'NetService')
        context.bot.send_message(chat_id = update.message.chat_id, text = 'کاربر عزیز در صورت نیاز میتوانید بروی دکمه ارسال شماره من کلیک کرده و شماره خود را ارسال کنید تا در اصرع وقت با شما تماس برقرار کنیم', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

    else:
        tlds= ['.am','.se','.ar','.at','.au','.bank','.be','.biz','.br','.by','.ca','.cc','.cl','.club','.cn','.co','.com','.cr','.cz','.de','.download','.edu','.education','.eu','.fi','.fm','.fr','.frl','.game','.global','.hk','.id','.ie','.im','.in','.info','.ink','.io','.ir','.is','.it','.jp','.kr','.kz','.link','.lt','.lv','.me','.mobi','.mu','.mx','.name','.net','.ninja','.nl','.nu','.nyc','.nz','.online','.org','.pe','.pl','.press','.pro','.pt','.pub','.pw','.rest','.ru','.rw','.sale', '.security','.sh','.site','.space','.store','.tech','.tel','.tickets','.trade','.tv','.ua','.uk','.us','.uz','.video','.website','.wiki','.work','.xyz','.za']

        if update.message.chat.id == 5189755201:
            for chatid in chatids:
                context.bot.forward_message(chat_id='{}'.format(chatid), from_chat_id=5189755201, message_id=update.message.message_id)
                context.bot.send_message(chat_id = update.message.chat_id, text = 'پیام شما ارسال شد')
        elif 'NS-' in update.message.text and len(update.message.text) == 12:
            clientcode = update.message.text.replace('NS-', '')
            clientsid = int('%s'%(clientcode[4:6]))
            clients.update({update.message.chat_id:clientsid})
            clientsdetails.update({update.message.chat_id:{'products':{'active':{}, 'inactive':{}}, 'domains':{'active':{}, 'inactive':{}}, 'tickets':{'open':{}, 'closed':{}}}})
            if update.message.chat_id in clients:
                keyboard = [
                ['دامنه ها', 'سرویس ها'],
                ['پشتیبانی', 'مالی'],
                ['خروج از ناحیه کاربری']
                ]
                context.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)
                context.bot.send_message(chat_id = update.message.chat_id, text = '{} {} عزیز،\nناحیه کاربری شما در نت سرویس با موفقیت به ربات تلگرام متصل شد \nاز این پس میتوانید با استفاده از دکمه ها به اطلاعات پنل مدیریت خود از طریق تلگرام دسترسی داشته باشید\n\n ❗️به دلیل افزایش امنیت حسابتان کد اتصال شما از صفحه چت حذف گردید'.format(update.message.from_user.first_name, update.message.from_user.last_name).replace('None', ''), reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))

        for i in tlds:
            if i in update.message.text.replace('http://', '').replace('https://', '').replace('www.', ''):
                domain = update.message.text.replace('http://', '').replace('https://', '').replace('www.', '')
                try:
                    chekdomain = whois.query(domain).name
                    if domain == chekdomain:
                        context.bot.send_message(chat_id = update.message.chat_id, text = '❗️ متاسفانه دامنه %s قبلا توسط شخص دیگری به ثبت رسیده است\n\nبرای جستجوی های بیشتر دامنه دیگری ارسال کنید.'%domain)
                except AttributeError:
                    keyboard =[
                    [InlineKeyboardButton('ثبت دامنه %s'%domain, 'https://me.netservice.shop/cart.php?a=add&domain=register&query=%s'%domain)]
                    ]
                    context.bot.send_message(chat_id = update.message.chat_id, text = '✅ خوشبختانه دامنه مورد نظر آزاد و قابل ثبت میباشد\n\nبرای ثبت بروی دکمه ثبت دامنه کلیک کنید', reply_markup = InlineKeyboardMarkup(keyboard))
                except:
                    keyboard =[
                    [InlineKeyboardButton('جستجوگر دامنه', 'https://me.netservice.shop/cart.php?a=add&domain=register')]
                    ]
                    context.bot.send_message(text = '❗️ متاسفانه جستجو با خطا مواجه شد،\n لطفا با کلیک بروی دکمه زیر از طریق سایت اقدام فرمایید' , chat_id = update.message.chat_id, reply_markup =  InlineKeyboardMarkup(keyboard))
                break
        else:
            if update.message.chat_id in clients:
                for tickets in whmcs.get_tickets(clientid=clientsid, status="Open"):
                    clientsdetails[update.message.chat_id]['tickets']['open'][tickets['tid']] = tickets['subject']
                whmcs.open_ticket(deptid=2,subject='ارتباط با پشتیبانی از طریق ربات تلگرام',message='%s'%update.message.text, clientid=clients[update.message.chat_id], priority='High')
                context.bot.forward_message(chat_id='5189755201', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
                context.bot.send_message(chat_id = update.message.chat_id, text = 'پیام شما برای پشتیبانان نت سرویس ارسال گردید و یک تیکت به شماره %s# در ناحیه کاربریتان ایجاد گردید'%(list(clientsdetails[update.message.chat_id]['tickets']['open'].items())[1][0]))
            else:
                context.bot.send_message(chat_id = update.message.chat_id, text = 'پیام شما با موفقیت برای پشتیبانی ارسال گردید، \nدر اصرع وقت با شما ارتباط برقرارا خواهم کرد')
                context.bot.forward_message(chat_id='5189755201', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
                with open('Message.txt', 'a', encoding="utf-8") as z:
                    z.write( 'آیدی:  {}    ||>>     {}\n\n____________________________________________________________________________________\n\n'.format(update.message.from_user.username, update.message.text))

def button_handler(update: Update, context: CallbackContext):
    if update.callback_query.data == 'aboutus':
        update.callback_query.bot.answer_callback_query(update.callback_query.id, text ='وبسایت نت سرویس زیر نظر شرکت دقیق ارقام پیشرو ، یک وب‌سایت فعال در حوزه رونق تجارت الکترونیکی و بازاریابی دیجیتالی می‌باشد', show_alert=True)

    elif update.callback_query.data == 'badge':
        keyboard = [
        [InlineKeyboardButton('نماد اعتماد الکترونیکی', 'https://trustseal.enamad.ir/?id=243802&Code=F9I0DqnqgeG8peV40EcU')],
        [InlineKeyboardButton('نماد ساماندهی', 'https://myket.ir/app/shop.netservice.me')],
        [InlineKeyboardButton('تاییدیه pay', 'https://pay.ir/trust/208331')],
        [InlineKeyboardButton('تاییدیه زرین پال', 'https://www.zarinpal.com/trustPage/netservice.shop')],
        [InlineKeyboardButton('بازگشت به درباره نت سرویس', callback_data = 'backabout')]
        ]
        context.bot.editMessageText(text = 'با کلیک بروی هریک از دکمه ها میتوانید جزییات بیشتر را مشاهده فرمایید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.callback_query.data == 'channels':
        keyboard = [
        [InlineKeyboardButton('بلاگ آموزشی', 'https://blog.netservice.shop')],
        [InlineKeyboardButton('پیج اینستاگرام', 'https://instagram.com/netserviceshop')],
        [InlineKeyboardButton('کانال اپارت', 'https://www.aparat.com/netserviceir')],
        [InlineKeyboardButton('صفحه توییتر', 'https://twitter.com/netserviceshop/')],
        [InlineKeyboardButton('صفحه ی لینکدین', 'https://www.linkedin.com/in/netserviceshop/')],
        [InlineKeyboardButton('بازگشت به درباره نت سرویس', callback_data = 'backabout')]
        ]
        context.bot.editMessageText(text = 'با دنبال کردن نت سرویس در صفحه های ارتباطی میتوانید از جدیدترین اخبار، جشنواره ها و تخفیفات و آگهی های استخدامی ما باخبر شوید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.callback_query.data == 'backabout':
        keyboard = [
        [InlineKeyboardButton('دقیق ارقام پیشرو', callback_data = 'aboutus')],
        [InlineKeyboardButton('مشاهده مجوز ها', callback_data = 'badge')],
        [InlineKeyboardButton('نت سرویس در رسانه ها', callback_data = 'channels')]
        ]
        context.bot.editMessageText(text = 'با کلیک بروی هریک از دکمه ها میتوانید جزییات بیشتر را مشاهده فرمایید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))

    elif update.callback_query.data == 'active_products':
        count = len(clientsdetails[update.callback_query.message.chat_id]['products']['active'])
        if count == 0:
            keyboard = [[InlineKeyboardButton('بازگشت به فهرست سرویس ها', callback_data = 'backtoprocucts')]]
            context.bot.editMessageText(text = '❕متاسفانه هیچ سرویس فعالی در ناحیه کاربری شما یافت نشد', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
        else:
            keyboard = []
            for i in clientsdetails[update.callback_query.message.chat_id]['products']['active']:
                keyboard.append([InlineKeyboardButton('%s'%clientsdetails[update.callback_query.message.chat_id]['products']['active'][i], callback_data = 'activeproduct%s'%count)])
                count = count-1
            keyboard.append([InlineKeyboardButton('بازگشت به فهرست سرویس ها', callback_data = 'backtoprocucts')])
            context.bot.editMessageText(text = 'تمامی سرویس های فعال شما در زیر لیست شده اند\n\nبا کلیک بروی هر یک از سرویس ها میتوانید جزییات بیشتری از سرویس خود بدست بیاورید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.callback_query.data == 'inactive_products':
        keyboard = []
        count = len(clientsdetails[update.callback_query.message.chat_id]['products']['inactive'])
        if count == 0:
            keyboard = [[InlineKeyboardButton('بازگشت به فهرست سرویس ها', callback_data = 'backtoprocucts')]]
            context.bot.editMessageText(text = '❕ خوشبخاته هیچ سرویس غیرفعالی در ناحیه کاربری شما یافت نشید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
        else:
            for i in clientsdetails[update.callback_query.message.chat_id]['products']['inactive']:
                keyboard.append([InlineKeyboardButton('%s'%clientsdetails[update.callback_query.message.chat_id]['products']['inactive'][i], callback_data = 'inactiveproduct%s'%count)])
                count = count-1
            keyboard.append([InlineKeyboardButton('بازگشت به فهرست سرویس ها', callback_data = 'backtoprocucts')])
            context.bot.editMessageText(text = 'تمامی سرویس های غیرفعال شما در زیر لیست شده اند\n\nبا کلیک بروی هر یک از سرویس ها میتوانید جزییات بیشتری از سرویس خود بدست بیاورید', chat_id = update.callback_query.message.chat_id, message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif update.callback_query.data == 'backtoprocucts':
        keyboard = [
            [InlineKeyboardButton('سرویس های فعال من', callback_data = 'active_products')],
            [InlineKeyboardButton('سرویس های معلق من', callback_data = 'inactive_products')]
            ]
        context.bot.editMessageText(chat_id = update.callback_query.message.chat_id, text = 'لطفا وضعیت سرویس های را جهت نمایش انتخاب فرمایید', message_id = update.callback_query.message.message_id, reply_markup =  InlineKeyboardMarkup(keyboard))
    elif 'product' in update.callback_query.data:
        number = int(update.callback_query.data.replace('inactiveproduct', '').replace('activeproduct', '')) - 1
        if 'inactive' in update.callback_query.data:
            update.callback_query.bot.answer_callback_query(update.callback_query.id, text ='\n نام سرویس:   %s\n\nشماره سفارش:   %s\n\nوضعیت سرویس:   غیرفعال'%(list(clientsdetails[update.callback_query.message.chat_id]['products']['inactive'].items())[::-1][number][1], list(clientsdetails[update.callback_query.message.chat_id]['products']['inactive'].items())[::-1][number][0]), show_alert=True)
        elif 'active' in update.callback_query.data:
            update.callback_query.bot.answer_callback_query(update.callback_query.id, text ='\n نام سرویس:   %s\n\nشماره سفارش:   %s\n\nوضعیت سرویس:   فعال'%(list(clientsdetails[update.callback_query.message.chat_id]['products']['active'].items())[::-1][number][1], list(clientsdetails[update.callback_query.message.chat_id]['products']['active'].items())[::-1][number][0]), show_alert=True)

    # else:
    #     update.callback_query.bot.answer_callback_query(update.callback_query.id, text ='دکمه ای که بروی آن کلیک کردید نامعتبر بود لاگ این اطلاعیه برای پشتیبانی ارسال میشود\n\nاز شما پوزش می طلبیم 🙏🏻'), show_alert=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
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
updater.dispatcher.add_handler(CommandHandler('myinfo', myinfo, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('webtech', webtech, pass_args= True))
updater.dispatcher.add_handler(CommandHandler('effect', effect))

updater.dispatcher.add_handler(MessageHandler(Filters.photo, effects))
updater.dispatcher.add_handler(MessageHandler(Filters.contact, contacts))
updater.dispatcher.add_handler(MessageHandler(Filters.all, main_keyboard))
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))

updater.start_polling()
updater.idle()
