from pyHoneygain import HoneyGain
from discord_webhook import DiscordWebhook
from datetime import date
import os

# Get jwt and webhook url from env var
JWT = os.getenv('JWT_TOKEN')
DISCORD = os.getenv('DISCORD_WEBHOOK')

user = HoneyGain()
user.set_jwt_token(JWT)

user_balance = "\nUser HG balance {}, JT balance {}".format(user.wallet_stats()["data"]["{}".format(date.today())]["hg_credits"], user.wallet_stats()["data"]["{}".format(date.today())]["jt_credits"])
honeypot_status = user.get_honeypot_status()
message = "error"
if str(honeypot_status["winning_credits"]) != "None":
    message = "{} already claimed the honeypot today.{}".format(user.me()['email'],  user_balance)
else:
    if honeypot_status["progress_bytes"] == honeypot_status["max_bytes"]:
        result = user.open_honeypot()
        if result["success"]:
            message = "Opened honeypot for {}, resulting in {} credits.{}".format(user.me()['email'], result["credits"], user_balance)
        else:
            message = "Couldn\'t open honeypot for {}, unknown error.{}".format(user.me()['email'], user_balance)
    else:
        message = "Couldn\'t open honeypot for {}, did not gather 15MB.{}\nProgress in bytes: {}/15000000".format(user.me()['email'], user_balance, user.get_honeypot_status()["progress_bytes"])

print(message)
webhook = DiscordWebhook(url=DISCORD, content='{}'.format(message))
response = webhook.execute()