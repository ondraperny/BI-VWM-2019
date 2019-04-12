import LoadInput
import Algorithm

def main():
    #TODO
    database = LoadInput.LoadDatabase()
    # LoadInput.PrintDatabase(database, 3)

    # links = LoadInput.LoadLinks()
    # LoadInput.PrintLinks(links, 3)

    result = Algorithm.FindUsersWithSameMoviesRated(database, 1)
    Algorithm.PrintUsersWithSameRatedMovies(result)


if __name__ == "__main__":
    main()