from flask import Flask, render_template
app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)
# render_template redirects the function to run the code in the respective .html files  listed

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
