from tempfile import NamedTemporaryFile
import shutil
import csv
import os

class IOClass:
    @staticmethod
    def print_database(database, how_many_users_print):
        """function to print part of database"""
        cnt = 0
        for user in database:
            if cnt >= how_many_users_print:
                break
            cnt += 1
            print(f"User with Id: {user}")
            for k, v in database[user].items():
                print(f"    Movie id: {k:6} was rated: {v:2}")

    @staticmethod
    def print_links(links, how_many_links_print):
        """print part of mapping od Id's to movie names"""
        cnt = 0
        for k in links:
            if cnt >= how_many_links_print:
                break
            cnt += 1

            print(f"Name of movie with Id: {k} is {links[k][0]:30}, tags: ", end="")
            for t in links[k][1]:
                print(f"{t} ", end="")
            print()

    @staticmethod
    def load_database():
        """load all data in structure dict(userId, dict(movieId, rating)) and return it"""
        with open('./data/ratings.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    database = {int(row['userId']): {row['movieId']: float(row['rating'])}}

                # add users and user
                if int(row['userId']) in database:
                    database[int(row['userId'])][row['movieId']] = float(row['rating'])
                else:
                    database[int(row['userId'])] = {row['movieId']: float(row['rating'])}

        return database

    @staticmethod
    def load_links():
        """load links to connect movieId's with real movie names"""
        with open('./data/movies.csv', mode='r', encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    links = {row['movieId']: (row['title'], row['genres'].split('|'))}

                links[row['movieId']] = (row['title'], row['genres'].split('|'))
        return links

    def update_rating(self, userId, movieId, newRating):
        # TODO checkovat jestli tam uz neni kdyz ho chci pridat
        filename = './data/test.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['userId', 'movieId', 'rating', 'timestamp']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['userId'] == str(userId) and row['movieId'] == str(movieId):
                    print('updating row', row['rating'])
                    row['rating'] = str(newRating)
                row = {'userId': row['userId'], 'movieId': row['movieId'], 'rating': row['rating'], 'timestamp': row['timestamp']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)

    def add_new_rating(self, userId, movieId, movieRating):
        row = [userId, movieId, movieRating, 0]

        with open('./data/test.csv', 'a') as csvFile:
            writer = csv.writer(csvFile, lineterminator=os.linesep)
            writer.writerow(row)

        csvFile.close()
