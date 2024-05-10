#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7043797215:AAFPaQ6-09l-3JcYKJI71XFbAqEswkiwF0A")
    API_ID = int(os.environ.get("API_ID", "26181533"))
    API_HASH = os.environ.get("API_HASH", "61f8a38f9d9d079100ba56fcbb9ea9b7")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6329158981")
