#CODES TEAM

import requests
import os
from user_agent import generate_user_agent

bot_url = "https://api.telegram.org/bot{}/sendMessage"

token = input('[×] ENTER YOUR BOT TOKEN »» ')
print()
print(' ━━━━━━━━━━━━━━━━━━━━━ ')
print()
chat_id = input('[×] ENTER YOUR  TELEGRAM ACCOUNT ID »» ')
print('Tele :@coder_amer & CH : @codes_team')

def send_message(token, chat_id, message):
    bot_url_with_token = bot_url.format(token)
    data = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.post(bot_url_with_token, data=data)
    return response

try:
    while True:
        user_agent = generate_user_agent()
        message_text = f"‌🇳‌🇪‌🇼         ━━━━━━━━━━━━━━━━━━━━━                                                 UserAgent =>  {user_agent}                                                ━━━━━━━━━━━━━━━━━━━━━                                    PY  : @coder_amer & CH : @codes_team"
        send_message(token, chat_id, message_text)
except KeyboardInterrupt:
    print('Error404')

#CODES TEAM