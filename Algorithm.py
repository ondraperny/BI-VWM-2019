from collections import OrderedDict
import LoadInput


class Recommendation:
    """class containing all methods used for recommending"""
    _ratings = (5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0)
    # _ratings = (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)

    def __init__(self, user):
        self.flag_print_in_console = True
        self.main_user = user

        self.map_movie_name_on_movie_id = OrderedDict()
        io = LoadInput.IOClass()

        # dict(tuple(one-title, second-list of genres))
        self.map_movie_name_on_movie_id = io.load_links()
        self.database = io.load_database()

    # TODO
    def final_recommendation(self, actionId):
        """control flow of recommendation functions, choose which scenario will be executed and return final results"""
        if actionId  == 0:
            res = self.spearman_similarity()
            closest_neighbours, distance_neighbours = self.most_similar_users(res)
            print(len(closest_neighbours) + len(distance_neighbours))
            quantity_dict, movie_list_users_dict = self.movies_to_recommend(closest_neighbours, distance_neighbours)
            res = self.recommended_movies(quantity_dict, movie_list_users_dict, closest_neighbours)
        elif actionId == 1:
            # best in genre recommendation
            ...
        elif actionId == 2:
            # best rated movie overall recommendation
            ...

        return res

    @staticmethod
    def print_users_with_same_movies_rated(result):
        for key, value in result.items():
            print(f"UserId: {key}, number of same rated movies: {value}")

        print(f"\nTotal number of users with at least one same movie rated: {len(result)}")
        print()

    def users_with_same_movies_rated(self):
        """find all users that have rated at least one common """
        # key = user, value = number of same movies rated with main user
        result = {}

        for user in self.database:
            # ignore when user is main_user's Id
            if user == self.main_user:
                continue

            for k in self.database[user]:
                if k in self.database[self.main_user]:
                    if user in result:
                        result[user] += 1
                    else:
                        result[user] = 1

        if self.flag_print_in_console:
            self.print_users_with_same_movies_rated(result)

        # dict(user_id : number_of_same_rated_movies)
        return result

    @staticmethod
    def print_common_rated_movies(main_user_dict, other_user_dict):
        print('Movie id: | main user: | other user:')
        print('------------------------------------')
        for keys in zip(main_user_dict, other_user_dict):
            print("%8s" % (keys[0]), "%10s" % main_user_dict[keys[0]], "%10s" % other_user_dict[keys[0]])

    def common_rated_movies(self, other_user):
        """return two dictionaries with movieId and its rating for main_user and other_user"""
        main_user_dict = OrderedDict()
        other_user_dict = OrderedDict()

        for movie in self.database[other_user]:
            if movie in self.database[self.main_user]:
                main_user_dict[movie] = self.database[self.main_user][movie]
                other_user_dict[movie] = self.database[other_user][movie]

        if self.flag_print_in_console:
            self.print_common_rated_movies(main_user_dict, other_user_dict)

        # dict(movie_id : user_rating_for_that_movie)
        return main_user_dict, other_user_dict

    def rank_x_and_y(self, main_user_dict, other_user_dict):
        """calculate rank vectors x and y for spearman formula"""
        rank_x_dict = main_user_dict.copy()
        rank_y_dict = other_user_dict.copy()

        n_main = 0
        n_other = 0

        # iterate through ratings 5 .. 0 and assign order numbers to each movie (based on its rating)
        for rating in self._ratings:
            rating_main = 0
            rating_othr = 0
            for keys in zip(main_user_dict, other_user_dict):
                if rating == main_user_dict[keys[0]]:
                    rating_main += 1
                if rating == other_user_dict[keys[0]]:
                    rating_othr += 1

            x_value = float(((n_main+1) + (n_main+rating_main))/2)
            y_value = float(((n_other+1) + (n_other+rating_othr))/2)

            n_main += rating_main
            n_other += rating_othr

            for keys in zip(main_user_dict, other_user_dict):
                if rating == main_user_dict[keys[0]]:
                    rank_x_dict[keys[0]] = x_value
                if rating == other_user_dict[keys[0]]:
                    rank_y_dict[keys[0]] = y_value

        if self.flag_print_in_console:
            self.print_common_rated_movies(rank_x_dict, rank_y_dict)

        # dict(user_id : x_or_y_rank_for_this_user)
        return rank_x_dict, rank_y_dict

    def d_squared(self, rank_x_dict, rank_y_dict):
        """calculate d squared vector for spearman formula"""
        d_squared_vector = []

        for (key1, value1), (key2, value2) in zip(rank_x_dict.items(), rank_y_dict.items()):
            d_squared_vector.append((float(value1) - float(value2))**2)

        if self.flag_print_in_console:
            print('Movie id: | main user: ')
            print('-----------------------')
            for index, (key, d_value) in enumerate(zip(rank_x_dict, d_squared_vector)):
                print("%8s" % key, "%10s" % d_squared_vector[index])

        # list(d_squared_values)
        return d_squared_vector

    # TODO
    @staticmethod
    def candidate_neightbours(neighbours):
        """choose neighbours with most same movies rated(with some maximum threshold of chosen neighbours), and filter
        out those whole number of same rated movies is very low, so not relevant"""
        # TODO optimalizace odstraneni nerelevantnich sousedu
        candidates_amount = len(neighbours)

        new_neighbours = {key:value for key,value in neighbours.items() if value > 2}
        # for key, value in neighbours.items():
        #     if value < 3:
        #         neighbours.pop(key)

        return new_neighbours

    def spearman_similarity(self):
        """finds spearman sim. between two users that have at least some same rated movies, where first user is main
        user and second is iterated from neighbours"""
        spearman_result = OrderedDict()
        neighbours = self.users_with_same_movies_rated()

        neighbours = self.candidate_neightbours(neighbours)

        # self.print_users_with_same_movies_rated(neighbours)
        # print(neighbours)

        for key, value in neighbours.items():
            # print("User:", key, "Value: ", value)
            main_user_dict, other_user_dict = self.common_rated_movies(key)

            # self.print_common_rated_movies(main_user_dict, other_user_dict)

            rank_x_dict, rank_y_dict = self.rank_x_and_y(main_user_dict, other_user_dict)
            # self.print_common_rated_movies(rank_x_dict, rank_y_dict)

            d_squared_vector = self.d_squared(rank_x_dict, rank_y_dict)
            current_n = len(rank_x_dict)
            # len(rank_x_dict)
            # spearman formula
            p = 1 - ((6 * sum(d_squared_vector)) / (current_n * ((current_n ** 2) - 1)))

            spearman_result[key] = p
            # print("Spearman:", p, '\n')
        # spearman_evaluation = neighbours.copy()
        if self.flag_print_in_console:
            print('Movie id: | main user: ')
            print('-----------------------')
            for key, value in spearman_result.items():
                print("%8s" % key, "%10s" % value)

        return spearman_result

    def most_similar_users(self, user_spearman_dict):
        """finds most similar users based on results from spearman_similarity() and cut of irrelevant users
        (on some threshold)"""

        closest_neighbours = {key:value for key, value in user_spearman_dict.items() if value > 0.5}
        distance_neighbours = {key:value for key, value in user_spearman_dict.items() if value < -0.5}

        # closest_neighbours = OrderedDict(sorted(closest_neighbours.items(), key=lambda x: x[1]))
        # distance_neighbours = OrderedDict(sorted(distance_neighbours.items(), key=lambda x: x[1]))

        print(closest_neighbours)
        print(distance_neighbours)

        # key = user, value = his relevance to main user
        return closest_neighbours, distance_neighbours

    def movies_to_recommend(self, closest_neighbours, distance_neighbours):
        """find movies that relevant neighbours rated but user didnt (at least some of them not every movie must have
        been seen by all neighbours, but those that were have higher priority, simply - relevance =
        for every neighbour that rated specific movie: relevance(of this specific movie) += neighbour_weight"""
        # closest_neighbours.update(distance_neighbours)

        quantity_dict = OrderedDict()
        movie_list_users_dict = {}

        for user in closest_neighbours:
            for movie in self.database[user]:
                if movie in quantity_dict:
                    quantity_dict[movie] += 1
                    movie_list_users_dict[movie].append(user)
                else:
                    quantity_dict[movie] = 1
                    movie_list_users_dict[movie] = [user]

        for movie in self.database[self.main_user]:
            quantity_dict.pop(movie, None)

        threshold = 3

        quantity_dict = {key:value for key, value in quantity_dict.items() if value > threshold}
        # quantity_dict = OrderedDict(sorted(quantity_dict.items(), key=lambda x: x[1], reverse=True))

        movie_list_users_dict = {key:value for key, value in movie_list_users_dict.items() if len(value) > threshold}

        print(movie_list_users_dict)
        print(quantity_dict)

        return quantity_dict, movie_list_users_dict

    def recommended_movies(self, quantity_dict, movie_list_users_dict, closest_neighbours):
        """from movies_to_recommend() find those movies that satisfy threshold (rating 3.5), those will be recommended,
        influence of rating from every neighbour is weighted by his relevance"""
        movie_to_recommend_dict = OrderedDict()

        for movie, users in movie_list_users_dict.items():
            weighted_denominator = 0
            coefficient = 0
            for user in users:
                coefficient += self.database[user][movie] * closest_neighbours[user]
                weighted_denominator += closest_neighbours[user]

            coefficient = coefficient / weighted_denominator
            movie_to_recommend_dict[movie] = coefficient

        movie_to_recommend_dict = OrderedDict(sorted(movie_to_recommend_dict.items(), key=lambda x: x[1], reverse=True))
        for movie, coefficient in movie_to_recommend_dict.items():
            print("Movie: %8s" % movie, "coefficient: %8.5f" % coefficient,
                  "quantity: %3s" % len(movie_list_users_dict[movie]))

        return movie_to_recommend_dict

    # SECOND SCENARIO
    # function from first scenario will suffice(if written properly)
    # in case we find relevant neighbours but they dont have any relevant same rated movies, we simply choose
    # best rated movies of closest neighbour(or more of them) with best ratings (mby this will be already
    # covered in first SCENARIO

    # THIRD SCENARIO
    def find_user_most_favourite_genre(self):
        # TODO
        for movie, rating in self.database[self.main_user]:
            ...

    def find_most_favourite_movies_in_genre(self):
        # TODO
        ...

    # FOURTH SCENARIO
    def find_best_rated_movie_overall(self):
        # required high rating
        # TODO
        result_dict = OrderedDict()
        for _, value in self.database.items():
            for movie, rating in value.items():
                if movie in result_dict:
                    result_dict[movie][0] += rating
                    result_dict[movie][1] += 1
                else:
                    result_dict[movie] = [rating, 1]

        # number of user that must hve rated given movie to be result valid
        threshold = 10
        result_dict = {key:value for key, value in result_dict.items() if value[1] > threshold}
        result_dict = OrderedDict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))

        for res in result_dict:
            print("Average rating of", res, "is", result_dict[res][0] / result_dict[res][1], "where",
                  result_dict[res][1], "people rated, with complete rating", result_dict[res][0])
        return result_dict

    def print_main_user_ratings(self):
        user_ratings = []
        for movie, rating in self.database[self.main_user].items():
            print(movie, rating, self.map_movie_name_on_movie_id[movie][0])
            user_ratings.append([movie, rating, self.map_movie_name_on_movie_id[movie][0]])

        # return list(list()), where in inner lists are 0 movieId, 1 movieRating, 2 movieName
        return user_ratings

# administrace uzivatelu, pamatovat si co jsem uz doporucil a nedoporucit to same, pridavani uzivatele do databaze a moznost menit hodnoceni v databazi


# print users rating