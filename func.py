import requests
from bs4 import BeautifulSoup
import random
import time
import csv

def m100(a):
    print(a)
    time.sleep(1)

    a = "<멜론 차트 TOP 100곡>"
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 100:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
        a = "<멜론 차트 TOP 100곡>"

        
def m50(b):
    print(b)
    time.sleep(1)

    b = "<멜론 차트 TOP 50곡>"
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
        b = "<멜론 차트 TOP 50곡>"

        
def m10(c):
    print(c)
    time.sleep(1)

    c= "<멜론차트 TOP 10곡>"
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 10:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
        c = "<멜론 차트 TOP 10곡>"

def m_random(d):
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
    url = 'https://www.melon.com/chart/index.htm'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.select('tr[data-song-no]')
        song_list = []

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))

        random_song = random.choice(song_list)
        time.sleep(1)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')
        d = "<AI 검색>"


def m_search(e):
        print(e)
        time.sleep(1)
        s = input("[검색하고 싶은 가수의 이름을 입력하세요.]: ")
        print(f"[<{s}>의 노래를 검색 중이에요...]")
        time.sleep(1)

        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
        url = 'https://www.melon.com/chart/index.htm'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.select('tr[data-song-no]')
        found_songs = []

        for song in songs:
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            if s.lower() in artist.lower():
                rank = song.select_one('span.rank').text.strip()
                title = song.select_one('div.ellipsis.rank01 a').text.strip()
                found_songs.append((rank, title, artist))

        if found_songs:
            print(f"[<{s}>의 노래 목록이에요.]")
            for song in found_songs:
                print(f'{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}')
        else:
            print(f"[TOP 100곡 내 <{s}>의 노래가 없어요.]")

        e = "<가수 이름 검색>"

def m_file(f):
        print(f)
        import requests
        from bs4 import BeautifulSoup

# 멜론 차트 URL
url = 'https://www.melon.com/chart/index.htm'

# HTTP 요청을 위한 헤더 (봇 차단 방지)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)

# 요청 성공 여부 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 노래 목록 선택
    songs = soup.select('tr[data-song-no]')
    song_list = []

    for song in songs:
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        song_list.append((rank, title, artist))

    # CSV 파일로 저장
    
    with open("melon_chart.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["순위", "제목", "아티스트"])
        writer.writerows(song_list)

    
    print("🎵 멜론 차트 100위 리스트를 'melon_chart.csv' 파일로 저장했습니다!")

    f = "<파일에 저장 (멜론100)>"