from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import  generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_user,login_remembered, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method== 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by (email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logiind satisfactoriamente', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('contrasea incorrecta, intenta otra vez', category='success')
        else:
            flash('Email incorrecto', category='error')

    
    return  render_template ("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():  
    logout_user()    
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():


    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by (email=email).first()

        if user:
            flash('Email ya existe',category='error')
        elif len(email) < 4:
            flash('Email debe contener mas de 4 caracteres', category='error')
        elif len(firstName)<2:
            flash('el primer nombre dee contener al menos 1 caracterer', category='error')
        elif password1 != password2:
            flash('la contrasea el no conciden', category='error')
        elif len(password1)< 7:
            flash('la contraseñ de contener minimo mas de 7 caracteres', category='error')
        else:
            new_user = User(email=email,first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remenber=True)
            flash('cuenta creada', category='succes')
            return redirect(url_for('views.home'))

    return render_template ("sign_up.html", user= current_user)

