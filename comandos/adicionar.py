from telegram import Update
from util.CheckAdmin import CheckAdmin
from util.youtube import youtubedownload
from Database import banido, permitido, post_grupo, post_lista

def adicionar(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    vazio = not "youtu.be" in update.message.text.lower()
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(vazio):
                    update.message.reply_text("<b>Informe um link do youtube válido!</b>","html")
                else:
                    link = update.message.text.split(" ")[1]
                    step1 = update.message.reply_text("<b>A mídia será adicionada à lista de reprodução quando o download for concluído!</b>","html")
                    dados = youtubedownload(link)
                    titulo = dados[0]
                    duracao = dados[1]
                    local = dados[2]
                    post_lista(titulo=titulo, link=link, local=f"downloads/{local}", grupo_id=grupo_id)
                    step1.edit_text(f"""<b>Download concluído!\n\nTítulo:</b> <a href="{link}">{titulo}</a>\n\n<b>Duração:</b> {duracao} <b>minutos.\n\nAdicionado com sucesso à lista de reprodução!</b>""","html")
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")
