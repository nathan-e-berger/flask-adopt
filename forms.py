"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Image URL")
    age = SelectField("Age",
                      choices = [("baby", "Baby"),
                                 ("young", "Young"),
                                 ("adult", "Adult"),
                                 ("senior", "Senior")])
    notes = StringField("Additional Information")