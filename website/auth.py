from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return  render_template ("login.html", text="Testing",user="jok")

@auth.route('/logout')
def logout():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fistaName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) > 4:
            flash('Email debe contener mas de 4 caracteres', category='error')
        elif len(firstName)<2:
            flash('el primer nombre dee contener al menos 1 caracterer', category='error')
        elif password1 != password2:
            flash('la contrasea el no conciden', category='error')
        elif len(password1)< 7:
            flash('la contraseñ de contener minimo mas de 7 caracteres', category='error')
            pass
        else:
            pass

        
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    return render_template ("sign_up.html")

