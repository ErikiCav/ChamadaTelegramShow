from telegram import Update
from util.CheckAdmin import CheckAdmin
from Database import banido, gerarid, permitido, post_grupo, post_lista
from tgcalls.tgcalls import client as USERBOT
from util.Conversao import Conversao
from os import remove

def tokenmidia(update: Update, context):
    grupo_id = update.message.chat.id
    post_grupo(grupo_id)
    user_id = update.message.from_user.id
    vazio = not "token" in update.message.text.lower()
    if not(f"{update.message.chat.type}" == "private"):
        if(permitido(CheckAdmin(update), user_id)):
            if(banido(grupo_id)):
                update.message.reply_text("<b>Este grupo está banido do bot!</b>","html")
            else:
                if(vazio):
                    update.message.reply_text("<b>Informe um token válido!</b>","html")
                else:
                    dados = update.message.text.split("/tokenmidia")[1].split("\n")
                    nome = dados[0].split("NOME: ")[1].replace("mkv","")
                    token = dados[1].split("TOKEN: ")[1]
                    idmkv = gerarid(34)
                    idmidia = gerarid(45)
                    step1 = update.message.reply_text("<b>A mídia será adicionada à lista de reprodução quando o download for concluído!</b>","html")
                    try:
                        USERBOT.download_media(message=token, file_name=f"path/{idmkv}.mkv")
                    except:
                        USERBOT.download_media(message=token, file_name=f"path/{idmkv}.mkv")
                    Conversao(idmkv, idmidia)
                    remove(f"path/{idmkv}.mkv")
                    post_lista(titulo=nome, link="none", local=f"downloads/{idmidia}".mvk, grupo_id=grupo_id)
                    step1.edit_text(f"""<b>Download concluído!\n\nTítulo:</b> <a href="none">{nome}</a>\n\n<b>Duração:</b> Só Deus sabe.<b>\n\nAdicionado com sucesso à lista de reprodução!</b>""","html")
    else:
        update.message.reply_text("""<b>Este comando só funciona em grupos!</b>""","html")
