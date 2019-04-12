
def PrintUsersWithSameRatedMovies(result):
    for k in result:
        if result[k] >= 2:
            print(f"UserId: {k}, number of same rated movies: {result[k]}")

    print(f"\nTotal number of users with at least one same movie rated: {len(result)}")
    print()


def FindUsersWithSameMoviesRated(database, userId):
    # dict with similarities
    result = {}

    for user in database:
        # ignore when user is userID
        if user == userId:
            continue

        for k in database[user]:
            if k in database[userId]:
                if user in result:
                    result[user] += 1
                else:
                    result[user] = 1

    return result

def MapMovieNamesOnId():
    # TODO
    ...


def FindBestMovieOverall():
    #required high ratin
    # TODO
    ...