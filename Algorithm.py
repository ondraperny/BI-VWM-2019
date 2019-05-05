class Recommendation:
    def __init__(self, user, database):
        self.user = user
        self.database = database
        # key = neighbours are users that will be used to recommend movie to main user
        # value = relevance of given neighbour
        self.neighbours = {}

    def final_recommendation(self):
        """control flow of recommendation functions, choose which scenario will be executed and return final results"""
        ...

    def print_users_with_same_movies_rated(self, result):
        for key, value in result.items():
            if value >= 2:
                print(f"UserId: {key}, number of same rated movies: {value}")

        print(f"\nTotal number of users with at least one same movie rated: {len(result)}")
        print()

    def find_users_with_same_movies_rated(self, database, user_id):
        """find all users that have rated at least one common """
        # dict with similarities
        result = {}

        for user in database:
            # ignore when user is user_id
            if user == user_id:
                continue

            for k in database[user]:
                if k in database[user_id]:
                    if user in result:
                        result[user] += 1
                    else:
                        result[user] = 1

        self.neighbours = result
        return result

    # FIRST SCENARIO
    def candidate_neightbours(self):
        """choose neighbours with most same movies rated(with some maximum threshold of chosen neighbours), and filter
        out those whole number of same rated movies is very low, so not relevant"""
        candidates_amount = len(self.neighbours)

    def spearman_similarity(self):
        """finds spearmen sim. between two users that have at least some same rated movies"""
        # TODO

    def most_similar_users(self):
        """finds most similar users based on results from spearman_similarity() and cut of irrelevant users
        (on some threshold)"""
        # TODO

    def movies_to_recommend(self):
        """find movies that relevant neighbours rated but user didnt (at least some of them not every movie must have
        been seen by all neighbours, but those that were have higher priority, simply - relevance =
        for every neighbour that rated specific movie: relevance(of this specific movie) += neighbour_weight"""
        # TODO

    def recommended_movies(self):
        """from movies_to_recommend() find those movies that satisfy threshold (rating 3.5), those will be recommended,
        influence of rating from every neighbour is weighted by his relevance"""
        # TODO

    # SECOND SCENARIO
        # function from first scenario will suffice(if written properly)
        # in case we find relevant neighbours but they dont have any relevant same rated movies, we simply choose
        # best rated movies of closest neighbour(or more of them) with best ratings (mby this will be already
        # covered in first SCENARIO

    # THIRD SCENARIO
    def find_user_most_favourite_genre(self):
        # TODO
        ...

    def find_most_favourite_movies_in_genre(self):
        # TODO
        ...

    # FOURTH SCENARIO
    def find_best_rated_movie_overall(self):
        # required high rating
        # TODO
        ...

    def map_movie_name_on_id(self):
        # TODO
        ...
