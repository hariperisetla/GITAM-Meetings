#pip install pyTelegramBotAPI

import telebot
import csv

def tbot(bot_token):

    bot = telebot.TeleBot(token=bot_token, parse_mode=None)
    @bot.message_handler(commands=["start", "meetings"])
    
    def sendmessage(message):
        if message.text=='/start':
            bot.reply_to(message,
            '''
            commands: /meetings
            ''')
        elif message.text == '/meetings':
            title = "GITAM Meetings"
            msg = '\n\n'
            with open('meet.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    msg += row[0]
                    msg += '\n'
                    msg += row[1]
                    msg += '\n'
                    msg += row[2]
                    msg += '\n\n'

            bot.reply_to(message, 
            
            title
            
            + msg +
            '''
            ''')
    print('Updated in Telegram')    
    bot.polling()
    
