from collections import OrderedDict


class Recommendation:
    _ratings = (5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0)

    def __init__(self, user, database):
        self.main_user = user
        self.database = database
        # key = neighbours are users that will be used to recommend movie to main user
        # value = relevance of given neighbour
        self.neighbours = {}

        self.main_user_dict = OrderedDict()
        self.other_user_dict = OrderedDict()


    def final_recommendation(self):
        """control flow of recommendation functions, choose which scenario will be executed and return final results"""
        ...

    def print_users_with_same_movies_rated(self, result):
        for key, value in result.items():
            if value >= 2:
                print(f"UserId: {key}, number of same rated movies: {value}")

        print(f"\nTotal number of users with at least one same movie rated: {len(result)}")
        print()

    def find_users_with_same_movies_rated(self):
        """find all users that have rated at least one common """
        # dict with similarities
        result = {}

        for user in self.database:
            # ignore when user is user_id
            if user == self.main_user:
                continue

            for k in self.database[user]:
                if k in self.database[self.main_user]:
                    if user in result:
                        result[user] += 1
                    else:
                        result[user] = 1

        self.neighbours = result
        return result

    def print_common_rated_movies(self):
        print('Main user            Other user')
        for keys in zip(self.main_user_dict, self.other_user_dict):
           print(keys[0], self.main_user_dict[keys[0]], keys[1], self.other_user_dict[keys[0]])

    def common_rated_movies(self, other_user):
        """return two dictionaries with movieId and its rating for given user"""

        for movie in self.database[other_user]:
            if movie in self.database[self.main_user]:
                self.main_user_dict[movie] = self.database[self.main_user][movie]
                self.other_user_dict[movie] = self.database[other_user][movie]

        return self.main_user_dict, self.other_user_dict

    def rank_x_and_y(self):
        rank_x_dict = self.main_user_dict.copy()
        rank_y_dict = self.other_user_dict.copy()

        n_main = 0
        n_othr = 0
        for rating in self._ratings:
            rating_main = 0
            rating_othr = 0
            for keys in zip(self.main_user_dict, self.other_user_dict):
                if rating == self.main_user_dict[keys[0]]:
                    rating_main += 1
                if rating == self.other_user_dict[keys[0]]:
                    rating_othr += 1

            x_value = float(((n_main+1) + (n_main+rating_main))/2)
            y_value = float(((n_othr+1) + (n_othr+rating_othr))/2)

            n_main += rating_main
            n_othr += rating_othr

            for keys in zip(self.main_user_dict, self.other_user_dict):
                if rating == self.main_user_dict[keys[0]]:
                    rank_x_dict[keys[0]] = x_value
                if rating == self.other_user_dict[keys[0]]:
                    rank_y_dict[keys[0]] = y_value

        print()
        for keys in zip(rank_x_dict, rank_y_dict):
           print(keys[0], rank_x_dict[keys[0]], keys[1], rank_y_dict[keys[0]])

    # FIRST SCENARIO
    def candidate_neightbours(self):
        """choose neighbours with most same movies rated(with some maximum threshold of chosen neighbours), and filter
        out those whole number of same rated movies is very low, so not relevant"""
        # TODO optimalizace odstraneni nerelevantnich sousedu
        candidates_amount = len(self.neighbours)

    def spearman_similarity(self):
        """finds spearmen sim. between two users that have at least some same rated movies, where first user is main
        user and second is iterated from neighbours"""
        for key, value in self.neighbours.items():
            # TODO
            ...

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
