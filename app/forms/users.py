#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__: Yxn
# date: 2016/10/18

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])