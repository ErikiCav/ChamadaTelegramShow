from os import remove
from Database import get_usada, post_grupo, banido, vazia, permitido
from comandos.controle import tocar
from telegram import Update
from util.CheckAdmin import CheckAdmin

def proximo(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(vazia(grupo_id)):
                    update.message.reply_text("<b>Não há nenhuma mídia na lista de reprodução.\nAdicione com /adicionar!</b>","html")
                else:
                    try:
                        step1 = update.message.reply_text("<b>Aguarde. Estou trocando de faixa!</b>","html")
                        tocar(grupo_id, step1)
                        local = get_usada(grupo_id)[1]
                        try:
                            remove(local)
                        except:
                            pass
                    except Exception as erro_id_1x:
                        step1.edit_text(f"<b>ERRO:</b> {erro_id_1x}\n\n<b>Dê /play novamente.</b>","html")
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")