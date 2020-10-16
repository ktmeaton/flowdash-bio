# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired

# Workflows


class WorkflowForm(FlaskForm):
    system = StringField("System", validators=[DataRequired()])
    node = StringField("Node", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    progress = IntegerField("Progress", validators=[DataRequired()])
    total_jobs = IntegerField("Total Jobs", validators=[DataRequired()])
    completed_jobs = IntegerField("Completed Jobs", validators=[DataRequired()])
    running_jobs = IntegerField("Running Jobs", validators=[DataRequired()])
    failed_jobs = IntegerField("Running Jobs", validators=[DataRequired()])
    start_date = DateField("Start Date", format="%Y-%m-%d", validators=[DataRequired()])
    end_date = DateField("End Date", format="%Y-%m-%d", validators=[DataRequired()])
    username = StringField("User", validators=[DataRequired()])
    submit = SubmitField("Submit")


class TestForm(FlaskForm):
    test = StringField("Test", validators=[DataRequired()])
    submit = SubmitField("Submit")
