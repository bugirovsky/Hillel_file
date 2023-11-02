import json
import os
import csv

#1) Перетворіть змінну ganres в словник. Використай бібліотеку json!.
ganres = '{"results":[{"genre":"Adventure"},{"genre":"Family"},{"genre":"Fantasy"},{"genre":"Crime"},{"genre":"Drama"},{"genre":"Comedy"},{"genre":"Animation"},{"genre":"Sci-Fi"},{"genre":"Sport"},{"genre":"Action"},{"genre":"Thriller"},{"genre":"Mystery"},{"genre":"Western"},{"genre":"Romance"},{"genre":"Biography"},{"genre":"Horror"},{"genre":"War"},{"genre":"Musical"},{"genre":"History"},{"genre":"Music"},{"genre":"Documentary"},{"genre":"Short"},{"genre":"Talk-Show"},{"genre":"Game-Show"},{"genre":"Reality-TV"},{"genre":"News"},{"genre":"Adult"}]}'

with open('films_data.json', 'r') as fd:
    films_data = json.load(fd)

genre_data = json.loads(ganres.replace("'", ' '))
root = os.getcwd()

directory_name = 'All Genre'
os.makedirs(directory_name, exist_ok=True)
os.chdir(directory_name)

#3) Для кожного жанру у змінній ganres створіть окрему дерикторію.
for file in genre_data["results"]:
    os.makedirs(f'{file["genre"]}')

#4)В кожній папці з жанорм створіть CSV файл, він буде зберігати інформацію про фільми. Файл має мати колонки: title, year, rating, type, ganres
os.chdir(root)
genres = os.listdir(os.path.join(os.getcwd(), 'All Genre'))
path = os.path.join(os.getcwd(), 'All Genre')
for genre in genres:
    filepath = os.path.join(path, genre)
    filename = filepath + f'/{genre}.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'year', 'rating', 'type', 'genres'])

#5)Відсортуй фільми у змінній films_data по жанрам. Тобто у файл csv з жанром запиши інформацію для кожнної колонки.
# Зверни увагу, що жанрів може бути кілька, тоді треба записати фільм у кілька CSV файлів при цьому колонка ganres має містити всі жанри фільму.
for film in films_data:
    gen = film['gen']
    for genre in gen:
        gnr = genre['genre']
        csv_path = os.path.join(path, gnr, f"{gnr}.csv")
        with open(csv_path, 'a', newline='', encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerow([film['title'], film['year'], film['rating'], film['type'], gnr])

