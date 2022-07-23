import os

def Conversao(idmkv, idmidia):
    os.popen(f"ffmpeg -i path/{idmkv}.mkv -map a? -map -m:language:eng -map -m:language:fra -map -m:language:spa -map -m:language:jpn -map v? -map s? -map d? -map t? -c:v copy -c:a copy downloads/{idmidia}.mkv")