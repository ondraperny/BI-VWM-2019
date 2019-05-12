from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class MyForm(FlaskForm):

    user = DecimalField('User ID', validators=[DataRequired(), NumberRange(min=1, max=610)])

    spearman_coefficient = DecimalField('Spearman coefficient', default=0.5, validators=[NumberRange(min=0, max=1)])

    min_same_rated_movies = IntegerField('Minimum of same movies rated', default=5, validators=[NumberRange(min=1, max=5000)])

    threshold_number_of_evaluators = IntegerField('Threshold # of evaluators', default=3)

    threshold_number_of_evaluators_global = IntegerField('Threshold # of evaluators (global)', default=30)

    number_to_recommend = IntegerField('# of movies to recommend', default=5, validators=[NumberRange(min=1, max=5000)])

    threshold_rating = DecimalField('Threshold # of rating', default=3.5, validators=[NumberRange(min=1, max=5)])

    submit = SubmitField("Send")


class EditForm(FlaskForm):

    user_id = IntegerField('User ID', validators=[DataRequired(), NumberRange(min=1, max=610)])

    movie_id = IntegerField('Movie ID', validators=[DataRequired(), NumberRange(min=1, max=193609)])

    new_rating = DecimalField('New Rating', validators=[NumberRange(min=1, max=5)])

    submit = SubmitField("Send")