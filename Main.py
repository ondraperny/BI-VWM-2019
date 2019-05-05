import LoadInput
import Algorithm


def main():
    # TODO
    database = LoadInput.load_database()
    recommend = Algorithm.Recommendation(1, database)
    # LoadInput.print_database(database, 3)

    # links = LoadInput.load_links()
    # LoadInput.print_links(links, 3)

    result = recommend.find_users_with_same_movies_rated()
    # recommend.print_users_with_same_movies_rated(result)

    userA, userB = recommend.common_rated_movies(3)

    recommend.print_common_rated_movies()
    recommend.rank_x_and_y()

if __name__ == "__main__":
    main()
