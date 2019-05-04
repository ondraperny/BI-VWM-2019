import csv


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


def load_links():
    with open('./data/movies.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                links = {row['movieId']: (row['title'], row['genres'].split('|'))}

            links[row['movieId']] = (row['title'], row['genres'].split('|'))

    return links
