import requests
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/a3e434401b08aba4ffa8").json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about_():
    return render_template('about.html')

@app.route('/contact')
def contact_():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)