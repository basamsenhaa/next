#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21157119"))
API_HASH = environ.get("API_HASH", "09c2a7c3e447d2139756c097e425d990")
BOT_TOKEN = environ.get("BOT_TOKEN", "8122751014:AAGJodRtSwE9cOQ6JDpOToFE7N73_ldwVuI")
OWNER = int(environ.get("OWNER", "-1002851481471"))
CREDIT = "𝐒нɑᎥ𝚝ɑη"
AUTH_USER = os.environ.get('AUTH_USERS', '-1002851481471').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
