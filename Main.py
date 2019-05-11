import Algorithm


def main():
    """Poznamky k API, vsechno co vracim uz je serazeny jak ma byt, takze staci jen vypsat,
    argumenty funkci jsou vzdy u kazde funkce napsane,
    co funkce vraceji vzdy popsano v komentari nad danou funkci,
    jiny nez tyhle 4 fce + konstruktor bys nemel potrebovat"""

    # prihlaseni uzivatele bude odpovidat vytvoreni classy Recommendation pro toho daneho uzivatele
    # tento konstruktor ma jeste dalsich 7 parametru(vsechny maji defaultni hodnoty, a jsou popsane v konstruktoru
    # recommendation classy, tyto parametry se daji menit v administratorskem modulu
    recommend = Algorithm.Recommendation(1)

    # vrati list listů s 3 hodnotami [movie_id, movie_name, movie_rating] pro vsechny filmi, ktere uzivatel ohodnotil
    # recommend.main_user_ratings()

    # vrati list listů s 3 hodnotami [movie_id, movie_name, expected_rating], kde expected_rating je cislo vyjadrujici
    # predpoklad ja by dany uzivatel ohodnotil tento film (urcuje prioritu pro recommendaci)
    recommend.final_recommendation()

    # vraci dictionary s movie_id a movie_name
    # recommend.all_movies()

    # vraci True pokud vstupni argumenty byli vporadku (rating v mezich, existuje zadane movie_id),
    # pokud vporadku nebyli vraci False
    # print(recommend.change_database(movie_id, new_rating))


if __name__ == "__main__":
    main()
