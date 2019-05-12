import os
from flaskr.Algorithm import Recommendation
from flask import Flask, render_template, flash, url_for, redirect
from flaskr.Forms import MyForm

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

        recommend = Algorithm.Recommendation(userid)
        films = recommend.main_user_ratings()
        recommendMovies = recommend.final_recommendation()
        return render_template("profile.html", films=films, recommendMovies=recommendMovies)
        #return redirect(url_for('profile'))
    else:
        flash(f'not Nice')
        print("not nice")
        userid = 1
    return render_template("home.html", form=form)


recommend = Algorithm.Recommendation(1)


films = recommend.main_user_ratings()
recommendMovies = recommend.final_recommendation()


@app.route('/profile')
def profile():
    return render_template("profile.html", films=films, recommendMovies=recommendMovies)


allMovies = recommend.all_movies()


@app.route('/movies')
def movies():
    return render_template("movies.html", films=allMovies)


@app.route('/recommend')
def recommend():
    return render_template("recommend.html", films=recommendMovies)
