
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

# FIRST SCENARIO
def spearman_similarity():
    """finds spearmen sim. between two users that have at least some same rated movies (threshold will be given)"""
    # TODO


def most_similar_users():
    """finds most similar users based on results from spearman_similarity() and cut of irrelevant users
    (on some threshold)"""
    # TODO


def movies_to_recommend():
    """find movies that relevant neighbours rated but user didnt (at least some of them not every movie must have
    been seen by all neighbours, but those that were have higher priority, simply - relevance =
    for every neighbour that rated specific movie: relevance(of this specific movie) += neighbour_weight"""
    # TODO


def recommended_movies():
    """from movies_to_recommend() find those movies that satisfy threshold (rating 3.5), those will be recommended,
    influence of rating from every neighbour is weighted by his relevance"""
    # TODO


# SECOND SCENARIO
    # function from first scenario will suffice(if written properly)
    # in case we find relevant neighbours but they dont have any relevant same rated movies, we simply choose
    # best rated movies of closest neighbour(or more of them) with best ratings (mby this will be already
    # covered in first SCENARIO

# THIRD SCENARIO
def find_user_most_favourite_genre():
    # TODO
    ...


def find_most_favourite_movies_in_genre():
    # TODO
    ...


# FOURTH SCENARIO
def find_best_rated_movie_overall():
    # required high rating
    # TODO
    ...


def map_movie_name_on_id():
    # TODO
    ...
