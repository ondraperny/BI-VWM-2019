from flaskr import Algorithm


def main():
    """Description of backend API, all results are sorted, ready to be only printed"""

    # user login equal creation of Recommendation class, where constructor's mandatory parameter is user's ID,
    # there are 7 other arbitrary parameters(parameters that alternate how recommending works)
    # all has default values and are described in detail in constructor
    # recommend = Algorithm.Recommendation(1)

    # return list of lists with 3 values: [movie_id, movie_name, movie_rating] for every movie that user rated
    # recommend.main_user_ratings()

    # return list of lists with 3 values: [movie_id, movie_name, expected_rating], where expected_rating is number
    # expressing assumption how would given user value this movie(which determines priority for recommendation)
    # recommend.final_recommendation()

    # return dictionary with movie_id and movie_name
    # recommend.all_movies()

    # change database record - return True if input arguments are valid (rating in boundaries, given movie_id exists)
    # otherwise return False
    # print(recommend.change_database(movie_id, new_rating))


if __name__ == "__main__":
    main()
