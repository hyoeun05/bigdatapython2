import random
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)
print(songs[1])

for song in songs:
    print(song) 

print("AI야 노래 한곡만 추천해줘")
print("""알겠습니다.""")

ai_song = random.choice(songs)

print(f"제가 추천한 곡은 {ai_song}입니다.")


# 리스트를 쓰는 이유
song1 = "a노래"
song2 = "b노래"
song3 = "c노래"

#print(song1)
#print(song2)
#print(song3)
