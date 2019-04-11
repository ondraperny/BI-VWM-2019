import LoadInput
import Algorithm

def main():
    #TODO
    database = LoadInput.LoadDatabase()
    # LoadInput.PrintDatabase(database, 3)

    # links = LoadInput.LoadLinks()
    # LoadInput.PrintLinks(links, 3)

    Algorithm.findUsersWithSameMoviesRated(database, 1)
    # Algorithm.findUsersWithSameMoviesRated(database, 2)
    # Algorithm.findUsersWithSameMoviesRated(database, 3)
    # Algorithm.findUsersWithSameMoviesRated(database, 4)
    # Algorithm.findUsersWithSameMoviesRated(database, 5)


if __name__ == "__main__":
    main()