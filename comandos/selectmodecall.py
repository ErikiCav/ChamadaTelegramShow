from Database import banido, permitido, post_grupo, get_modo, post_modo
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from util.CheckAdmin import CheckAdmin_query

def selectmodecall(update: Update, context):
    query = update.callback_query
    grupo_id = query.message.chat.id
    user_id = query.from_user.id
    tipo = query.message.chat.type
    post_grupo(grupo_id)
    if not(f"{tipo}" == "private"):
        if(permitido(CheckAdmin_query(query), user_id)):
            if(banido(grupo_id)):
                query.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(get_modo(grupo_id) == "video"):
                    keyboard = [[InlineKeyboardButton(text="Modo de som e vídeo-⬛", callback_data="trocarmododechamada")], [InlineKeyboardButton(text="Modo de som-✅", callback_data="trocarmododechamada")]]
                    post_modo(grupo_id, "audio")
                else:
                    keyboard = [[InlineKeyboardButton(text="Modo de som e vídeo-✅", callback_data="trocarmododechamada")], [InlineKeyboardButton(text="Modo de som-⬛", callback_data="trocarmododechamada")]]
                    post_modo(grupo_id, "video")
                markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text("""<b>O modo selecionado atualmente está marcado com "✅", troque clicando no modo desejado!</b>""","html", reply_markup=markup)
    else:
        query.edit_message_text("""<b>Este comando só funciona em grupos!</b>""","html")