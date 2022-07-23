import pytube
from Database import gerarid

def youtubedownload(link):
    pytubed = pytube.YouTube(link)
    id = gerarid(25)
    titulo = pytubed.title
    duracao = (pytubed.length) / 60.00
    pytubed.streams.get_lowest_resolution().download(output_path="downloads/",filename=id)
    return titulo, ("{:,.2f}".format(duracao).replace(".",":")), id
