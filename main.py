from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CSRFProtect
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
import form
from config import DevelopmentConfig
from model import db
from model import User
from flask_mail import Mail
from flask_mail import Message
import threading
from flask import copy_current_request_context
from model import Comment
from helper import date_format

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
mail = Mail()

def send_email(user_email,username):
    msg = Message('Gracias por tu registro!',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[user_email])

    msg.html = render_template('email.html', user=username)
    mail.send(msg)

@app.route("/",methods=['GET','POST'])
def index():
    #form
    comment_form = form.commentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        user_id = session['id']
        comment = Comment(user_id=user_id,
                          name=comment_form.name.data,
                          text=comment_form.message.data)
        db.session.add(comment)
        db.session.commit()

    return render_template("index.html",form=comment_form)

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['index']:
        return redirect(url_for("login"))
    elif 'username' not in session and request.endpoint in ['reviews']:
        return redirect(url_for("login"))
    elif 'username' in session and request.endpoint in['register', 'login']:
        return redirect(url_for("index"))


@app.route("/register", methods= ["GET","POST"])
def register():
    register_form = form.register(request.form)
    if request.method == 'POST' and register_form.validate():
        user = User(register_form.username.data,
                    register_form.email.data,
                    register_form.password.data)
        db.session.add(user)
        db.session.commit()

        @copy_current_request_context
        def send_message(email,username):
            send_email(email,username)

        sender = threading.Thread(name='mail_sender',target=send_message,
                                  args=(user.email,user.username))
        sender.start()

        success_message = "Registrado en la base de datos"
        flash(success_message)

        return redirect(url_for("login"))

    title = "Registrese por favor"
    return render_template("register.html", title=title, form = register_form)

@app.route("/login",  methods= ["GET","POST"])
def login():
    login_form = form.login(request.form)
    if request.method == "POST" and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username = username).first()
        if user is not None and user.verify_password(password):
            session['username'] = username
            session['id'] = user.id
            return redirect(url_for("index"))
        else:
            error = "Usuario o contraseña no validos"
            flash(error)

    title = "Logeate por favor"
    return render_template("login.html", title= title, form = login_form )

@app.route("/logout")
def logout():
    if 'username' in session:
        session.clear()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route("/reviews/",methods=['GET'])
@app.route("/reviews/<int:page>",methods=['GET'])
def reviews(page = 1):
    title = "Comentarios"
    per_page = 7
    comment_list = Comment.query.join(User).add_columns(User.username,
                                                        Comment.text,
                                                        Comment.created_date).paginate(page,per_page,False)
    return render_template("reviews.html", title = title, comments = comment_list, date_format= date_format)


if __name__ == "__main__":
    csrf.init_app(app) #Iniciar la configuracion con lo que ya tenemos
    db.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port = 8000)



