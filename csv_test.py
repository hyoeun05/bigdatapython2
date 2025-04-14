import csv

data_to_write =[
['순위', '제목' '가수']
[1. ,'1노래' '1가수']
[2. ,'2노래' '2가수']
[3. ,'3노래' '3가수']
]

# CSV 파일 쓰기
with open('example.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 헤더 작성
    writer.writerow(['Name', 'Age', 'City'])
    # 데이터 작성
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'London'])
    writer.writerow(['Charlie', 22, 'Seoul'])

print("CSV 파일 작성 완료!")

# CSV 파일 읽기
with open('example.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # 내용 읽기
    for row in reader:
        print(row)

print("CSV 파일 읽기 완료!")