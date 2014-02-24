from flask.ext.wtf import Form
from wtforms import TextField, BlooleanField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BlooleanField('remember_me',default = False)