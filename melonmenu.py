print("=================")
print ("1. 멜론 100")
print ("2. 멜론 50")
print ("3. 멜론 10")
print ("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("=================")

# 메뉴선택(숫자입력):1
n = input("메뉴선택(숫자입력):")
print(f"당신이 입력한 값은? {n}")


# 만약에 1을 입력하면
# 멜론 100 출력

if n == 1:
    print("멜론 100")
import requests

# 멜론 100위 차트 API (2024년 기준, 변경될 가능성 있음)
url = "https://www.melon.com/chart/"

# 멜론은 User-Agent가 없으면 차단할 수 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text

    # BeautifulSoup으로 파싱
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # 제목과 가수 정보 찾기
    songs = soup.select("div.ellipsis.rank01 > span > a")  # 노래 제목
    artists = soup.select("div.ellipsis.rank02 > span")    # 가수 이름

    # 100위까지 출력
    for rank, (song, artist) in enumerate(zip(songs, artists), start=1):
        print(f"{rank}위: {song.text} - {artist.text}")


# 만약에 2를 입력하면
# 멜론 50 출력
elif n == 2:
    print("멜론 50")
    import requests

# 멜론 100위 차트 URL
url = "https://www.melon.com/chart/"

# 멜론은 User-Agent가 없으면 차단될 수 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text

    # BeautifulSoup으로 파싱
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # 제목과 가수 정보 찾기
    songs = soup.select("div.ellipsis.rank01 > span > a")  # 노래 제목
    artists = soup.select("div.ellipsis.rank02 > span")    # 가수 이름

    # 50위까지 출력
    print("멜론 50")
    for rank, (song, artist) in enumerate(zip(songs[:50], artists[:50]), start=1):
        print(f"{rank}위: {song.text} - {artist.text}")

# 만약에 3을 입력하면
# 멜론 10 출력

elif n == 3:
    print("멜론 10")
    import requests

# 멜론 100위 차트 URL
url = "https://www.melon.com/chart/"

# 멜론은 User-Agent가 없으면 차단될 수 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text

    # BeautifulSoup으로 파싱
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # 제목과 가수 정보 찾기
    songs = soup.select("div.ellipsis.rank01 > span > a")  # 노래 제목
    artists = soup.select("div.ellipsis.rank02 > span")    # 가수 이름

    # 10위까지 출력
    print("멜론 10")
    for rank, (song, artist) in enumerate(zip(songs[:10], artists[:10]), start=1):
        print(f"{rank}위: {song.text} - {artist.text}")