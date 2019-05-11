import LoadInput
import Algorithm


def main():
    # prihlaseni uzivatele bude odpovidat vytvoreni classy Recommendation pro toho daneho uzivatele

    recommend = Algorithm.Recommendation(3)
    ## recommend.users_with_same_movies_rated()
    # main_user_dict, other_user_dict = recommend.common_rated_movies(1)
    # rank_x_dict, rank_y_dict = recommend.rank_x_and_y(main_user_dict, other_user_dict)
    # recommend.d_squared(rank_x_dict, rank_y_dict)
    # recommend.spearman_similarity()
    # recommend.find_best_rated_movie_overall()

    recommend.final_recommendation()


    # recommend.main_user_ratings()

    # recommend.add_genre(genre) prida zanr
    # recommend.final_recommendation()


    # io.update_rating(user_id, movie_id, new_rating)
    # kdyz vrati False, update se nepovedl

    # io.add_new_rating(user_id, movie_id, new_rating)
    # kdyz vrati False, pridani se nepovedlo


if __name__ == "__main__":
    main()
