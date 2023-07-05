from flask import Flask,render_template

app=Flask(__name__)

posts=[
  {
    "title":"Blog Post1",
    "author":"Abhishek",
    "date":"July 7th, 2023",
    "content":"Post content"
  },
  {
    "title":"Blog Post2",
    "author":"Abhi",
    "date":"July 7th, 2023",
    "content":"Post content Img"
  }
]

@app.route("/")
@app.route("/homepage")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)