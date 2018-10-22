# Imports

import telegram
import configparser

# End of imports

# Declerations

config = configparser.ConfigParser()
config.read("config.ini")

tbot = telegram.Bot(token=config["Telegram"]["token"])