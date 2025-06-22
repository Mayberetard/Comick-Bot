#___Every Variable Is Mandatory/Required So Fill Those With Causion___#


import logging

#--------------------------------------------------------------------------------------------------------------------------#
# Telegram API credentials
API_ID = "" # Replace with your API_ID 
API_HASH = "" # Replace with your HASH
BOT_TOKEN = "" # Replace with your BOT TOKEN
BOT_UN = "maybemangaBot" # Replace with your BOT Username Without @


# MongoDB setup
DB_URL = "" # Replace with your mongo db url
DB_NAME = "Comick" # Do Need To Change This 

# Admin and Channel details
ADMIN = ""  # Replace with your Telegram user ID
CHANNEL = "maybe_retard" # Replace with your force sub channel username. add bot as admin in yourforce sub channel before start the bot  
DB_CHANNEL_UN = "dbchannel12"  # Replace with your File store channel username .Must Be Public
IS_NOTIFY = "False"   # "True" or "False". If "True" Then It Will Send New Aired Chapter Notification In DM

# Download directory
DOWNLOAD_DIRECTORY = "./downloads" # Do Need To Change This

# Copyright Banner
BANNER_PATH = "banner.jpg" # Replace with your Copyright Banner Path

#--------------------------------------------------------------------------------------------------------------------------#

# Logging configuration
LOGGING_CONFIG = {  # Do Not Change This
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'handlers': [
        logging.FileHandler("manga_bot.log"),
        logging.StreamHandler()
    ]
}
