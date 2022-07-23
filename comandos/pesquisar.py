from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from Database import gerarid
from tgcalls.tgcalls import client as USERBOT

def pesquisar(update: Update, context):
    dados = []
    texto = update.inline_query.query.split(" ", 1)
    if(texto[1] == ""):
        update.inline_query.answer(switch_pm_text="Digite o ID ou username do canal, o filme ou série.", results=dados, switch_pm_parameter="vaziotexto")
        return
    else:
        canal = texto[0]
        for dados_pesquisados in USERBOT.search_messages(f"{canal}", query=texto[1], limit=30):
            if(f"{dados_pesquisados.document}" == "None"):
                pass
            else:
                nome = dados_pesquisados.document.file_name
                id = dados_pesquisados.document.file_id
                dados.append(InlineQueryResultArticle(thumb_url="https://www.cvv.org.br/wp-content/uploads/2021/05/music-heart.jpg", description="Canal: Acervo da Tv.", title=f"{nome}", input_message_content=InputTextMessageContent(f"/tokenmidia <b>NOME: </b>{nome}\n<b>TOKEN: </b>{id}","html"), id=str(gerarid(34))))
        update.inline_query.answer(results=dados, cache_time=0)
