from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):

    user = DecimalField('User', validators=[DataRequired()])

    spearman_coefficient = DecimalField('Spearman coefficient')

    min_same_rated_movies = IntegerField('Minimum of same movies rated')

    threshold_number_of_evaluators = DecimalField('Threshold # of evaluators')

    threshold_number_of_evaluators_global = DecimalField('Threshold # of evaluators (global)')

    number_to_recommend = IntegerField('# of movies to recommend')

    threshold_rating = DecimalField('Threshold # of rating')

    submit = SubmitField("Send")
