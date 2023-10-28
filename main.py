import os
import json
import string

films_titles = json.load(open('films_titles.json', encoding='utf-8'))
films_awards = json.load(open('films_awards.json', encoding='utf-8'))

new_films_awards = {}
for item in films_awards:
    award_list = []
    for award in item['results']:
        award_list.append({'award_name': award['award_name'], 'award': award['award'], 'type': award['type']})
    sorted_dict = sorted(award_list, key=lambda d: d['award_name'])

    title = item['results'][0]['movie']['title']
    new_films_awards[title] = sorted_dict

directory_name = 'Harry Potter'
os.makedirs(directory_name, exist_ok=True)

os.chdir(directory_name)
for item in films_titles['results']:
    title = item['title']
    if ':' in title:
        title_directory = title.replace(':', ' ')
    else:
        title_directory = title

    os.makedirs(title_directory, exist_ok=True)
    os.chdir(title_directory)

    for letter in string.ascii_uppercase:
        os.makedirs(letter, exist_ok=True)
    awards_list = new_films_awards[title]

    for award in awards_list:
        directory = award['award_name'][0]
        os.chdir(directory)

        with open(f"{award['award_name']}.txt", 'a', encoding='utf-8') as f:
            f.write(award['award'])
        os.chdir('..')
    os.chdir('..')
