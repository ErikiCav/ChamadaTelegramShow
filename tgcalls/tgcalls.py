from os import remove
from Database import vazia, get_usada, get_lista, get_modo
from pyrogram import Client
import config, time, telegram
from pytgcalls import PyTgCalls, StreamType, PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioVideoPiped, AudioPiped

client = Client(":memory", config.API_ID, config.API_HASH, session_string=config.SESSION_STRING)

bot = telegram.Bot(config.TOKEN_BOT)

pytgcalls = PyTgCalls(client)

filter = []

def CheckDual(chat_id):
  quantidade = 0
  for id in filter:
    if(f"{chat_id}" in f"{id}"):
      quantidade += 1
  return quantidade

@pytgcalls.on_stream_end()
async def on_stream_end(clientd: PyTgCalls, update: Update):
  chat_id = update.chat_id
  filter.append(chat_id)
  if(get_modo(chat_id) == "video"):
    if(CheckDual(chat_id) == 2):
      filter.remove(chat_id)
      filter.remove(chat_id)
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
        try:
          await pytgcalls.join_group_call(chat_id,AudioVideoPiped(local),stream_type=StreamType().pulse_stream,)
        except:
          await pytgcalls.join_group_call(chat_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
        bot.send_message(chat_id, f"""<b>Próxima mídia tocando:</b> <a href="{link}">{titulo}</a>.\n\n<b>Use /listas para listar as listas de reprodução!</b>""","html")
        local = get_usada(chat_id)[1]
        remove(local)

  else:
    filter.remove(chat_id)
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
      await pytgcalls.join_group_call(chat_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
      bot.send_message(chat_id, f"""<b>Próxima mídia tocando:</b> <a href="{link}">{titulo}</a>.\n\n<b>Use /listas para listar as listas de reprodução!</b>""","html")
      local = get_usada(chat_id)[1]
      remove(local)

run = pytgcalls.start()
