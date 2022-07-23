from Database import banido, permitido, post_grupo, get_modo
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from util.CheckAdmin import CheckAdmin

def modo(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(get_modo(grupo_id) == "video"):
                    keyboard = [[InlineKeyboardButton(text="Modo de som e vídeo-✅", callback_data="trocarmododechamada")], [InlineKeyboardButton(text="Modo de som-⬛", callback_data="trocarmododechamada")]]
                else:
                    keyboard = [[InlineKeyboardButton(text="Modo de som e vídeo-⬛", callback_data="trocarmododechamada")], [InlineKeyboardButton(text="Modo de som-✅", callback_data="trocarmododechamada")]]
                markup = InlineKeyboardMarkup(keyboard)
                update.message.reply_text("""<b>O modo selecionado atualmente está marcado com "✅", troque clicando no modo desejado!</b>""","html", reply_markup=markup)
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")