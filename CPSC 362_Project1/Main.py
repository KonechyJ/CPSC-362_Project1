from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "cf74f95f26104490b2578bd8d837797a"


#this a list of dictionaries currently being used to store "posts"
posts = [
    {
        "author": "Joshua Konechy",
        "title": "Post 1",
        "content": "First Item",
        "date_posted": "September 10, 2021"
    },
    {
        "author": "Jane Doe",
        "title": "Post 2",
        "content": "Second Item",
        "date_posted": "September 11, 2021"
    }
]

#@app.route is a way to create a website directory
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
# render_template redirects the function to run the code in the respective .html files  listed

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@auction.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
