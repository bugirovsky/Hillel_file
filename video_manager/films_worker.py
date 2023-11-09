import os.path


class Film:
    def __init__(self, title, description, director, year, trailer):
        self.title = title
        self.description = description
        self.year = year
        self.director = director
        self.trailer = trailer
        self.storage_address = ''
        self.upload_file()

    def upload_file(self):
        folder = self.title[0].upper()
        self.storage_address = f'../../video_manager/film_storage/{folder}/{self.title}.txt'
        open(os.path.join(self.storage_address), 'w').close()

    def get_film_address(self):
        print(self.storage_address)

    def give_film(self):
        print(f'Name Film: ' + self.title + "\n" +
              f'\t\tDescription: ' + self.description +
              f'\n\t\tDirector: ' + self.director +
              f'\n\t\tYear: ' + str(self.year) +
              f'\n\t\tTrailer: ' + self.trailer + '\n')



