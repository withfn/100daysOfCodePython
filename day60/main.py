import requests
import smtplib
from flask import Flask, render_template, request

my_email = ""
password = ""

posts = requests.get("https://api.npoint.io/a3e434401b08aba4ffa8").json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about_():
    return render_template('about.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/contact', methods=['GET','POST'])
def contact_():
    if request.method == 'GET':
        return render_template('contact.html', send=False)
    
    elif request.method == 'POST':    
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        text = f'name: {name}\nemail: {email}\nphone: {phone}\nmessage: {message}'
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, 
                                msg=f"Subject:testezada\n\n{text}")
        return render_template('contact.html', send=True)
    
    else:
        return None
    


if __name__ == "__main__":
    app.run(debug=True)