from telegram import Update
from Database import post_user
import config


def adduser(update: Update, context):
    if(f"{update.message.from_user.id}" in f"{config.USER_ROOT}"):
        post_user(update.message.reply_to_message.from_user.id)
        update.message.reply_text("<b>Usuário adicionado!</b>","html")