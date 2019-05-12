import os
from flaskr.Algorithm import Recommendation
from flask import Flask, render_template


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
@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")

# testovaci data


#films = [[1, 'Avatar', 5], [2, 'Gavatar', 4], [3, 'V for Vendeta', 5], [4, 'Thor: Dark Word', 3], [5, 'The Shining', 4]]

recommend = Algorithm.Recommendation(1)
films = recommend.main_user_ratings()

@app.route('/profile')
def profile():
    return render_template("profile.html", films=films)


recommendMovies = recommend.final_recommendation()


@app.route('/recommend')
def recommend():
    return render_template("recommend.html", films=recommendMovies)



