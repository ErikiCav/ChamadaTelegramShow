from telegram import Update
from util.CheckAdmin import CheckAdmin
from Database import banido, permitido, post_grupo, post_lista

def adicionar_live(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    vazio = not "http" in update.message.text.lower()
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(vazio):
                    update.message.reply_text("<b>Informe um link de live válido!</b>","html")
                else:
                    link = update.message.text.split(" ")[1].replace(" ","")
                    step1 = update.message.reply_text("<b>A mídia será adicionada à lista de reprodução!</b>","html")
                    post_lista(titulo="Live Stream", link=link, local=f"{link}", grupo_id=grupo_id)
                    step1.edit_text(f"""<b>Mídia adicionada à lista!\n\nTítulo:</b> <a href="{link}">Live Stream</a>\n\n<b>Duração:</b> Só Deus sabe.<b>\n\nAdicionada com sucesso à lista de reprodução!</b>""","html")
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")