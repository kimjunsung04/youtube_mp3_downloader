import youtube_dl
import wget
from youtubesearchpython import VideosSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

url = input("다운받을 유뷰브 링크 or 영상제목을 입력해주세요 : ")

if "http" in url:
    ydl = youtube_dl.YoutubeDL({"outtmpl": "%(id)s%(ext)s"})
    ydl.add_default_info_extractors()
    result = ydl.extract_info(url, download=False)
else:
    videosSearch = VideosSearch(f"{url}", limit=1)
    ytde = videosSearch.result()
    y_id = ytde["result"][0]["id"]
    url = f"https://www.youtube.com/watch?v={y_id}"

    ydl = youtube_dl.YoutubeDL({"outtmpl": "%(id)s%(ext)s"})
    ydl.add_default_info_extractors()
    result = ydl.extract_info(url, download=False)

m_url = result
title = m_url["title"]
m_url = m_url["formats"][1]["url"]
file = wget.download(m_url, f"./{title}.mp3")