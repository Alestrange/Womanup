import os
from flask import Flask, render_template, redirect, request
from data import db_session
from forms.user import LoginForm, RegisterForm
from data.users import User
from data.tenders import Tenders
from flask_login import LoginManager, login_user, login_required, logout_user
import flask_login


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/tenders_db.db")
    app.run(debug=True)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    user_loged = flask_login.current_user.is_authenticated
    print(user_loged)
    return render_template("index.html", user_loged=user_loged)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print(1)
            return redirect("/index")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        if db_sess.query(User).filter(form.expert_password.data != "expert_password").first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Неправильный код эксперта")
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/tenders', methods=['GET', 'POST'])
def tenders():
    db_sess = db_session.create_session()
    tenders = db_sess.query(Tenders)
    return render_template('tenders.html', tenders=tenders)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    main()