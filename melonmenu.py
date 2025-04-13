import requests
from bs4 import BeautifulSoup
import random

def get_melon_chart():
    # 멜론 차트 URL
    url = "https://www.melon.com/chart/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        songs = soup.select("div.ellipsis.rank01 > span > a")
        artists = soup.select("div.ellipsis.rank02 > span")
        chart_data = [{"song": song.text, "artist": artist.text} for song, artist in zip(songs, artists)]
        return chart_data
    else:
        print("멜론 차트 데이터를 가져오지 못했습니다.")
        return []

def search_artist(chart_data):
    artist_name = input("검색할 가수 이름을 입력하세요: ")
    print(f"\n'{artist_name}'의 검색 결과:")
    results = [entry for entry in chart_data if artist_name.lower() in entry["artist"].lower()]
    if results:
        for i, entry in enumerate(results, start=1):
            print(f"{i}. {entry['song']} - {entry['artist']}")
    else:
        print("검색 결과가 없습니다.")

def main_menu():
    print("=================")
    print("1. 멜론 100")
    print("2. 멜론 50")
    print("3. 멜론 10")
    print("4. AI 추천 노래")
    print("5. 가수 이름 검색")
    print("=================")

def main():
    chart_data = get_melon_chart()  # 데이터를 한 번만 가져오기
    if not chart_data:
        return

    main_menu()
    try:
        n = int(input("메뉴선택(숫자입력): "))
    except ValueError:
        print("숫자를 입력해주세요!")
        return

    if n == 1:
        print("\n멜론 100")
        for rank, entry in enumerate(chart_data[:100], start=1):
            print(f"{rank}위: {entry['song']} - {entry['artist']}")
    elif n == 2:
        print("\n멜론 50")
        for rank, entry in enumerate(chart_data[:50], start=1):
            print(f"{rank}위: {entry['song']} - {entry['artist']}")
    elif n == 3:
        print("\n멜론 10")
        for rank, entry in enumerate(chart_data[:10], start=1):
            print(f"{rank}위: {entry['song']} - {entry['artist']}")
    elif n == 4:
        print("\nAI 추천 노래")
        random_song = random.choice(chart_data)
        print(f"추천 곡: {random_song['song']} - {random_song['artist']}")
    elif n == 5:
        search_artist(chart_data)
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()