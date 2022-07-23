from comandos.Listas import Listas
from comandos.adduser import adduser
from comandos.adicionar import adicionar
from comandos.adicionar_live import adicionar_live
from comandos.modo import modo
from comandos.pesquisar import pesquisar
from comandos.proximo import proximo
from comandos.rmuser import rmuser
from comandos.selectmodecall import selectmodecall
from comandos.stop import stop
from comandos.tokenmidia import tokenmidia
from config import TOKEN_BOT
from telegram.ext import CommandHandler, Updater, InlineQueryHandler, CallbackQueryHandler
from comandos.play import play
from pytgcalls import idle
from Database import criarpadrao

bot = Updater(TOKEN_BOT)

criarpadrao()
bot.dispatcher.add_handler(CommandHandler("play", play, run_async=True))
bot.dispatcher.add_handler(CommandHandler("stop", stop, run_async=True))
bot.dispatcher.add_handler(CommandHandler("proximo", proximo, run_async=True))
bot.dispatcher.add_handler(CommandHandler("listas", Listas, run_async=True))
bot.dispatcher.add_handler(CommandHandler("modo", modo, run_async=True))
bot.dispatcher.add_handler(CommandHandler("tokenmidia", tokenmidia, run_async=True))
bot.dispatcher.add_handler(CommandHandler("adicionar", adicionar, run_async=True))
bot.dispatcher.add_handler(CommandHandler("adicionar_live", adicionar_live, run_async=True))
bot.dispatcher.add_handler(CommandHandler("adduser", adduser, run_async=True))
bot.dispatcher.add_handler(CommandHandler("rmuser", rmuser, run_async=True))
bot.dispatcher.add_handler(InlineQueryHandler(pesquisar, run_async=True))
bot.dispatcher.add_handler(CallbackQueryHandler(selectmodecall, pattern="trocarmododechamada", run_async=True))
bot.start_polling(drop_pending_updates=True)
idle()