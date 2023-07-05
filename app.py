from flask import Flask,render_template, url_for, flash, redirect, get_flashed_messages
from forms import Registeration, Login
app=Flask(__name__)

# to protect you application from attact
app.config['SECRET_KEY']='f1c8bce515b93991c0cb2cca8b84feda'

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
    return render_template("about.html",title="About Page")

@app.route("/register", methods=['GET','POST'])
def register():
    form=Registeration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Registeration",form=form)

@app.route("/login")
def login():
    form=Login()
    return render_template("login.html",title="Login",form=form)


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)