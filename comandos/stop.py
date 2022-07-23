from os import remove
from Database import get_usada, post_grupo, banido, permitido
from comandos.controle import sair
from telegram import Update
from util.CheckAdmin import CheckAdmin

def stop(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                update.message.reply_text("<b>Comando atendido!</b>","html")
                sair(grupo_id)
                try:
                    local = get_usada(grupo_id)[1]
                    remove(local)
                except:
                    pass
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")