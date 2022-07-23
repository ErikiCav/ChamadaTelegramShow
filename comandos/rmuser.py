from telegram import Update
from Database import delete_user
import config


def rmuser(update: Update, context):
    if(f"{update.message.from_user.id}" in f"{config.USER_ROOT}"):
        delete_user(update.message.reply_to_message.from_user.id)
        update.message.reply_text("<b>Usuário removido!</b>","html")