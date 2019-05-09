import LoadInput
import Algorithm


def main():
    # TODO

    # prihlaseni uzivatele bude odpovidat vytvoreni classy Recommendation pro toho daneho uzivatele

    io = LoadInput.IOClass()

    # io.update_rating(1, 1, 4)
    # io.add_new_rating(1524, 1111, 2)

    recommend = Algorithm.Recommendation(3)

    recommend.print_main_user_ratings()

    # recommend.add_genre(genre) prida zanr
    # recommend.final_recommendation(actionId)
    # TODO domyslet actionId parametr
    # actionId == 0 ... spearman, actionId == 1 ... vyhledani nejlepsiho filmu v zanru, actionId == 2 vyhledani globalne nejlepsi film

    # io.update_rating(user_id, movie_id, new_rating)
    # kdyz vrati False, update se nepovedl

    # io.add_new_rating(user_id, movie_id, new_rating)
    # kdyz vrati False, pridani se nepovedlo


if __name__ == "__main__":
    main()
