import LoadInput
import Algorithm


def main():
    # TODO
    database = LoadInput.load_database()
    recommend = Algorithm.Recommendation(1, database)
    # LoadInput.print_database(database, 3)

    # links = LoadInput.load_links()
    # LoadInput.print_links(links, 3)

    result = recommend.find_users_with_same_movies_rated(database, 1)
    recommend.print_users_with_same_movies_rated(result)


if __name__ == "__main__":
    main()
