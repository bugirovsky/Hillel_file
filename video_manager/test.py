import os
import string

from films_worker import Film

directory_name = "film_storage"
os.getcwd()
os.makedirs(directory_name)

os.chdir(directory_name)
for letter in string.ascii_uppercase:
    os.makedirs(letter)

if __name__ == '__main__':
    film = Film('Momento', "The film continues to tell the story of a boy wizard", "Chris Columbus", 2002,
                'https://www.wizardingworld.com/')
    film.get_film_address()
