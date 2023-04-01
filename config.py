#!/usr/bin/env python3


### Importing
from os import environ

class Config(object):
    TG_BOT_TOKEN = "6144753157:AAHfsBvjQWdaOAI1My-6JVeB5zbdD9hWTXM" # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = 27885485 # Get this value from https://my.telegram.org/apps
    
    API_HASH = "7dd9974c713787410beae4a295cc1e2d" # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = 5663539940 # Your(owner's) telegram id
    
    MONGO_STR = "mongodb+srv://sanmart02:sanmart02@uploader.qn5vziv.mongodb.net/?retryWrites=true&w=majority" # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    
