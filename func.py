import requests
from bs4 import BeautifulSoup
import random
import time
import csv

# 멜론 차트 크롤링 함수
def get_melon_chart(limit):
    url = 'https://www.melon.com/chart/index.htm'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        
        song_list = [(song.select_one('span.rank').text.strip(),
                      song.select_one('div.ellipsis.rank01 a').text.strip(),
                      song.select_one('div.ellipsis.rank02 a').text.strip()) 
                     for song in songs[:limit]]

        return song_list
    else:
        print(f"🚨 웹 페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
        return []

# TOP 100 출력
def m100():
    print("\n🎵 멜론 차트 TOP 100곡")
    time.sleep(1)
    song_list = get_melon_chart(100)
    for song in song_list:
        print(f"{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}")

# TOP 50 출력
def m50():
    print("\n🎵 멜론 차트 TOP 50곡")
    time.sleep(1)
    song_list = get_melon_chart(50)
    for song in song_list:
        print(f"{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}")

# TOP 10 출력
def m10():
    print("\n🎵 멜론 차트 TOP 10곡")
    time.sleep(1)
    song_list = get_melon_chart(10)
    for song in song_list:
        print(f"{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}")

# 랜덤 노래 추천
def m_random():
    print("\n🎵 랜덤 노래 추천!")
    time.sleep(1)
    song_list = get_melon_chart(100)
    if song_list:
        random_song = random.choice(song_list)
        print(f"\n🎵 추천 곡: {random_song[1]} | 아티스트: {random_song[2]}")
    else:
        print("🚨 추천할 노래가 없습니다.")

# 가수 검색
def m_search():
    s = input("\n🔎 검색할 가수 이름을 입력하세요: ")
    print(f"🎵 <{s}>의 노래 검색 중...")
    time.sleep(1)
    
    song_list = get_melon_chart(100)
    found_songs = [song for song in song_list if s.lower() in song[2].lower()]

    if found_songs:
        print(f"\n🎵 <{s}>의 노래 목록:")
        for song in found_songs:
            print(f"{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}")
    else:
        print(f"🚨 TOP 100곡 내 <{s}>의 노래가 없습니다.")

# 파일로 저장
def m_file():
    print("\n💾 멜론 차트 100곡을 CSV 파일로 저장 중...")
    time.sleep(1)
    
    song_list = get_melon_chart(100)
    
    with open("melon_chart.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["순위", "제목", "아티스트"])
        writer.writerows(song_list)

    print("✅ 'melon_chart.csv' 파일 저장 완료!")

# 🔥 사용자 입력 기반 실행
while True:
    print("\n")