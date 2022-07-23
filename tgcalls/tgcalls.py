from os import remove
from Database import vazia, get_usada, get_lista, get_modo
from pyrogram import Client
import config
import time
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped, AudioPiped
import telegram

client = Client(":memory", config.API_ID, config.API_HASH, session_string=config.SESSION_STRING)

bot = telegram.Bot(config.TOKEN_BOT)

pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(clientd: PyTgCalls, update: Update):
  chat_id = update.chat_id
  if(vazia(chat_id)):
    try:
      await pytgcalls.leave_group_call(chat_id)
    except:
      pass
    bot.send_message(chat_id, "<b>O bot saiu da chamada pois não há nada na fila de reprodução!</b>","html")
    local = get_usada(chat_id)[1]
    remove(local)
  else:
    dados = get_lista(chat_id)
    titulo = dados[1]
    link = dados[2]
    local = dados[3]
    try:
      await pytgcalls.leave_group_call(chat_id)
    except:
      pass
    time.sleep(2)
    if(get_modo(chat_id)=="video"):
      try:
        await pytgcalls.join_group_call(chat_id,AudioVideoPiped(local),stream_type=StreamType().pulse_stream,)
      except:
        await pytgcalls.join_group_call(chat_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
    else:
      await pytgcalls.join_group_call(chat_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
    bot.send_message(chat_id, f"""<b>Próxima mídia tocando:</b> <a href="{link}">{titulo}</a>.\n\n<b>Use /listas para listar as listas de reprodução!</b>""","html")
    local = get_usada(chat_id)[1]
    remove(local)

run = pytgcalls.start()
