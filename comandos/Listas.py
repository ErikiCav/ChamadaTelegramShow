from Database import get_listas, post_grupo, banido, permitido
from telegram import Update
from util.CheckAdmin import CheckAdmin

def Listas(update: Update, context):
    contador = 0
    listas = ""
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                for dados in get_listas(grupo_id):
                    titulo = dados[1]
                    link = dados[2]
                    contador += 1
                    listas += f"""<b>{contador}-</b> <a href="{link}">{titulo}</a>\n"""
                if(contador==0):
                    update.message.reply_text("<b>Nenhuma lista encontrada!</b>","html")
                else:
                    update.message.reply_text(f"<b>Esta é a lista de reprodução deste grupo!</b>\n\n{listas}""","html")
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")