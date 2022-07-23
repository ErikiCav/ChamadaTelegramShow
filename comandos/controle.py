from pytgcalls import StreamType
import tgcalls, time
from pytgcalls.types.input_stream import AudioVideoPiped, AudioPiped
from Database import get_lista, get_modo

def sair(grupo_id):
    try:
        tgcalls.pytgcalls.leave_group_call(grupo_id)
    except:
        pass

def entrar_video(grupo_id):
    dados = get_lista(grupo_id)
    titulo = dados[1]
    link = dados[2]
    local = dados[3]

    try:
        tgcalls.pytgcalls.join_group_call(grupo_id, AudioVideoPiped(local), stream_type=StreamType().pulse_stream, )
    except:
        tgcalls.pytgcalls.join_group_call(grupo_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
    return titulo, link

def entrar_audio(grupo_id):
    dados = get_lista(grupo_id)
    titulo = dados[1]
    link = dados[2]
    local = dados[3]

    tgcalls.pytgcalls.join_group_call(grupo_id, AudioPiped(local), stream_type=StreamType().pulse_stream, )
    return titulo, link

def tocar(grupo_id, mensagem):
    sair(grupo_id)
    time.sleep(3)
    if(get_modo(grupo_id) == "video"):
        dados = entrar_video(grupo_id)
        titulo = dados[0]
        link = dados[1]
    else:
        entrar_audio(grupo_id)
        titulo = dados[0]
        link = dados[1]
    mensagem.edit_text(f"""<b>Mídia tocando:</b> <a href="{link}">{titulo}</a>.\n\n<b>Use /listas para listar as listas de reprodução!</b>""","html")
    
