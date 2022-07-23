from wtforms import Form, EmailField, StringField, PasswordField,TextAreaField
from wtforms import validators
from wtforms import HiddenField
from model import User

def length_honeypot(form,field):
    if len(field.data) > 0:
        raise validators.ValidationError("El campo tiene que estar vacio")

class register(Form):
    username = StringField("Nombre de usuario:",[
        validators.length(min=4, max=25),
        validators.data_required(message= "El username es requierido")
    ])
    email = EmailField("Correo electronico:",[
        validators.email(),
        validators.data_required()
    ])
    password = PasswordField("Contraseña:",[
        validators.data_required(),
        validators.length(min=6)
    ])
    honeypot = HiddenField("",[
        length_honeypot
    ])

    def validate_username(form,field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError("El username ya se encuentra registrado")

    def validate_email(form,field):
        email = field.data
        email = User.query.filter_by(email = email).first()
        if email is not None:
            raise validators.ValidationError("El email ya se encuentra registrado")

class login(Form):
    username = StringField("Nombre de usuario:",[
        validators.length(min=4,max=25),
        validators.data_required()
    ])
    password = PasswordField("Contraseña:",[
        validators.data_required()
    ])
    honeypot = HiddenField("",[
        length_honeypot
    ])

class commentForm(Form):
    name = StringField("Ingrese su nombre:",[
        validators.length(min=4),
        validators.data_required()
    ])
    email = EmailField("Ingrese su email:",[
        validators.email(),
        validators.data_required()
    ])
    message = TextAreaField("Ingrese su mensaje:",[
        validators.data_required()
    ])
    honeypot= HiddenField("",[
        length_honeypot
    ])


