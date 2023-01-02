from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_MOVIE_KEY = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, default=None)
    ranking = db.Column(db.Integer, default=None)
    review = db.Column(db.String(300), default=None)
    img_url = db.Column(db.String(400), nullable=False)
    
    def __repr__(self):
        return f'<movies {self.title}>'


class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
     #This line creates a list of all the movies sorted by rating
    movie_list = Movie.query.order_by(Movie.rating).all()
    
    #This line loops through all the movies
    for i in range(len(movie_list)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    return render_template("index.html", movie_list = movie_list)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = str(form.title.data).replace(' ', '%20')
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_MOVIE_KEY}&language=en-US&query={title}&page=1&include_adult=false"
        response = requests.get(url=url).json()
        return render_template('select.html', movies_title = response)
        
    return render_template('add.html', form=form)        


@app.route("/select", methods=['GET', 'POST'])
def select():
    movie_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_MOVIE_KEY}&language=en-US"
    response = requests.get(url=url).json()
    
    title = response["title"]
    img_url = f'https://image.tmdb.org/t/p/original{response["poster_path"]}'
    year = int(str(response["release_date"][0:4]))
    description = response["overview"]
    
    new_movie = Movie(
    title=title,
    year=year,
    description=description,
    img_url=img_url
    )
    
    db.session.add(new_movie)
    db.session.commit()
    
    movie = Movie.query.filter_by(title=title).first()
    return redirect(url_for('edit', id=movie.id))
    
    

if __name__ == '__main__':
    app.run(debug=True)
