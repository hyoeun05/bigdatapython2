import requests

# 도시별 좌표 저장
city_coordinates = {
    "서울": (37.5665, 126.9780),
    "부산": (35.1796, 129.0756),
    "Tokyo": (35.682839, 139.759455),
    "New York": (40.712776, -74.005974),
    "London": (51.507351, -0.127758)
}

def get_coordinates(city_name):
    """도시 이름을 받아 좌표를 반환"""
    return city_coordinates.get(city_name, (None, None))

def get_weather(lat, lon):
    """좌표를 이용해 날씨 정보를 가져옴"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code != 200:
        print("날씨 API 요청 실패")
        return {}

    try:
        data = response.json()
        return data.get('current_weather', {})
    except requests.exceptions.JSONDecodeError:
        print("날씨 데이터 해석 오류 발생")
        return {}

def main():
    city = input("날씨를 확인할 도시명을 입력하세요: ")
    lat, lon = get_coordinates(city)

    if lat is None or lon is None:
        print("해당 도시를 찾을 수 없습니다.")
        return

    weather = get_weather(lat, lon)
    if weather:
        print(f"\n[{city}]의 현재 날씨:")
        print(f"기온: {weather['temperature']}°C")
        print(f"풍속: {weather['windspeed']} km/h")
        print(f"강수량: {weather.get('precipitation', 0)} mm")  # 강수량 추가
        print(f"날씨 코드: {weather['weathercode']}")
    else:
        print("날씨 정보를 가져오지 못했습니다.")

if __name__ == "__main__":
    main()