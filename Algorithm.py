
def print_users_with_same_movies_rated(result):
    for k in result:
        if result[k] >= 2:
            print(f"UserId: {k}, number of same rated movies: {result[k]}")

    print(f"\nTotal number of users with at least one same movie rated: {len(result)}")
    print()


def find_users_with_same_movies_rated(database, user_id):
    # dict with similarities
    result = {}

    for user in database:
        # ignore when user is user_id
        if user == user_id:
            continue

        for k in database[user]:
            if k in database[user_id]:
                if user in result:
                    result[user] += 1
                else:
                    result[user] = 1

    return result


def map_movie_name_on_id():
    # TODO
    ...


def find_best_rated_movie_overall():
    # required high rating
    # TODO
    ...


def find_user_most_favourite_genre():
    # TODO
    ...


def find_most_favourite_movies_in_genre():
    # TODO
    ...
