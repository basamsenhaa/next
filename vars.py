import os
from os import environ

API_ID = int(environ.get("API_ID", "21157119"))
API_HASH = environ.get("API_HASH", "09c2a7c3e447d2139756c097e425d990")
BOT_TOKEN = environ.get("BOT_TOKEN", "8122751014:AAGJodRtSwE9cOQ6JDpOToFE7N73_ldwVuI")
OWNER = int(environ.get("OWNER", "8085923848"))
CREDIT = "𝐒нɑᎥ𝚝ɑη"
# Get authorized users from environment variable, default to OWNER if not set
AUTH_USER = os.environ.get('AUTH_USERS', '8085923848').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
# Ensure OWNER is always included in AUTH_USERS
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
# Get channel ID from environment variable, convert to int if provided
CHANNEL_ID = environ.get("-1002851481471")
if CHANNEL_ID:
    CHANNEL_ID = int(CHANNEL_ID)
else:
    CHANNEL_ID = None
# Combine authorized users and channel ID for authorization checks
AUTHORIZED_ENTITIES = AUTH_USERS.copy()
if CHANNEL_ID:
    AUTHORIZED_ENTITIES.append(CHANNEL_ID)
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
