from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import URL
import csv
from cafe import Cafe

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(require_tld=True, message='You need add the entire url')])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    power_rating = SelectField('Power Socket Availability', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        coffee_rating = f'{int(str(form.coffee_rating.data)) * "☕"}'
        wifi_rating = f'{int(str(form.wifi_rating.data)) * "💪"}'
        power_rating = f'{int(str(form.power_rating.data)) * "🔌"}'
        data = [str(form.cafe.data), str(form.location.data), str(form.open_time.data), str(form.close_time.data), 
                coffee_rating, wifi_rating, power_rating]
        with open('cafe-data.csv', 'a', newline='', encoding="utf8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
            
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
    cafe_objects = []
    for cafe in list_of_rows:
        cafe_object = Cafe(cafe[0], cafe[1], cafe[2], cafe[3], cafe[4], cafe[5], cafe[6])
        cafe_objects.append(cafe_object)
    
    return render_template('cafes.html', cafes=cafe_objects)


if __name__ == '__main__':
    app.run(debug=True)
