from pytube import YouTube


def length(url):
    yt = YouTube(url)
    return yt.length
