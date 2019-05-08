from tempfile import NamedTemporaryFile
import shutil
import csv
import os


class IOClass:
    """class that contains all functions that are used for IO operations with the file"""

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

    @staticmethod
    def update_rating(user_id, movie_id, new_rating):
        filename = './data/movies.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['userId', 'movieId', 'rating', 'timestamp']

        flag = True
        with open(filename, 'r') as csv_file, tempfile:
            reader = csv.DictReader(csv_file, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['userId'] == str(user_id) and row['movieId'] == str(movie_id):
                    flag = False
                    print('updating row', row['rating'])
                    row['rating'] = str(new_rating)
                row = {'userId': row['userId'], 'movieId': row['movieId'], 'rating': row['rating'],
                       'timestamp': row['timestamp']}
                writer.writerow(row)

        if flag:
            print("Wrong userId and movieId combination - database was not changed")

        shutil.move(tempfile.name, filename)

    @staticmethod
    def add_new_rating(user_id, movie_id, new_rating):
        # TODO checkovat jestli tam uz neni kdyz ho chci pridat

        row = [user_id, movie_id, new_rating, 0]

        with open('./data/movies.csv', 'a') as csvFile:
            writer = csv.writer(csvFile, lineterminator=os.linesep)
            writer.writerow(row)

        csvFile.close()
