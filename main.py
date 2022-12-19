from pytube import YouTube


def download(url):
    youtube_object = YouTube(url)
    youtube_object = youtube_object.streams.get_highest_resolution()

    try:
        youtube_object.download()
    except:
        print("Ocorreu algum erro com o download do video!")
    print("Tudo certo,donload completo!!")


url = input("Coloque o link do video aqui! URL:")
download(url)
