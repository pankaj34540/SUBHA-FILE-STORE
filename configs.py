import os

class Config(object):
  API_ID = int(os.environ.get("27112188", ""))
  API_HASH = os.environ.get("2b5f6870e9bef1d12bea4c9a9fdf13ef", "")
  BOT_TOKEN = os.environ.get("6562429690:AAGrU2H63E2tw3KYjP94NGJgdLq5g_AQYow", "")
  BOT_USERNAME = os.environ.get("subha_robot", "")
  DB_CHANNEL = int(os.environ.get("-1001903213496 -1002142848563 -1002056600050", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shareus.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "44wmpwKuZVbwqrM1jQO0Se0h3xY2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5830314143"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://pdas966846:<password>@cluster0.bnbswj6.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002013661113")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "5830314143"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{subha_robot})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_SUBHA_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/Miss_rosebotss7)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Miss_rosebotss7)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
