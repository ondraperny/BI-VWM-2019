import os
from flaskr.Algorithm import Recommendation
from flask import Flask, render_template, flash, url_for, redirect
from flaskr.Forms import MyForm, EditForm

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    TEMPLATES_AUTO_RELOAD='TRUE',
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# a simple page that says home
@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Nice')
        print("nice")
        print(form.user.data)
        userid = form.user.data
        spearman_coefficient = form.spearman_coefficient.data
        min_same_rated_movies = form.min_same_rated_movies.data
        threshold_number_of_evaluators = form.threshold_number_of_evaluators.data
        threshold_number_of_evaluators_global = form.threshold_number_of_evaluators_global.data
        number_to_recommend = form.number_to_recommend.data
        threshold_rating = form.threshold_rating.data

        recommend = Algorithm.Recommendation(userid, False, spearman_coefficient, min_same_rated_movies, threshold_number_of_evaluators, threshold_number_of_evaluators_global, number_to_recommend, threshold_rating)
        films = recommend.main_user_ratings()
        recommendMovies = recommend.final_recommendation()

        return render_template("profile.html", films=films, recommendMovies=recommendMovies, user=userid)
        #return redirect(url_for('profile'))
    else:
        flash(f'not Nice')
        print("not nice")
    return render_template("home.html", form=form)





@app.route('/profile')
def profile():
    recommend = Algorithm.Recommendation(1)
    films = recommend.main_user_ratings()
    recommendMovies = recommend.final_recommendation()
    return render_template("profile.html", films=films, recommendMovies=recommendMovies)


@app.route('/editRating', methods=['GET', 'POST'])
def editRating():
    form1 = EditForm()
    if form1.validate_on_submit():
        recommend = Algorithm.Recommendation(form1.user_id.data)
        if recommend.change_database(form1.movie_id.data, form1.new_rating.data):
            return redirect(url_for('profile'))

    return render_template("editRating.html", form=form1)

recommend = Algorithm.Recommendation(1)
films = recommend.main_user_ratings()
recommendMovies = recommend.final_recommendation()
allMovies = recommend.all_movies()


@app.route('/movies')
def movies():
    return render_template("movies.html", films=allMovies)


@app.route('/recommend')
def recommend():
    return render_template("recommend.html", films=recommendMovies)
