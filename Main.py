import LoadInput
import Algorithm


def main():
    # TODO
    database = LoadInput.load_database()
    recommend = Algorithm.Recommendation(3, database)
    # LoadInput.print_database(database, 3)

    # links = LoadInput.load_links()
    # LoadInput.print_links(links, 3)

    recommend.tmp_wrapper()

if __name__ == "__main__":
    main()
