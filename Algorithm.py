def findUsersWithSameMoviesRated(database, userId):
    # dict with similarities
    result = {}

    for user in database:
        # ignore when user is userID
        if user == userId:
            continue

        # print(user)

        for k in database[user]:
            # print("   " + k)
            # for k1 in database[userId]:
            if k in database[userId]:
                # if k == k1:
                if user in result:
                    result[user] += 1
                else:
                    result[user] = 1

    for k in result:
        # print(f"{k} a {result[k]}")
        if result[k] >= 2:
            print(f"{k} a {result[k]}")
    # print(result)
