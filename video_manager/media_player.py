from films_worker import Film


class Player(Film):
    def __init__(self, name, video_link, number_of_users, duration, creator, title):
        self.name = name
        self.video_link = video_link
        self.number_of_users = number_of_users
        self.duration = duration
        self.creator = creator
        self.title = title

    def play(self):
        print("Video started: ", self.title)

    def stop(self):
        print("Pause")

    def info(self):
        print(f'Name Player: ' + self.title + "\n" +
              f'\t\tLink: ' + self.video_link +
              f'\n\t\tNumber user: ' + str(self.number_of_users) +
              f'\n\t\tDuration: ' + self.duration +
              f'\n\t\tCreator: ' + self.creator + "\n")
