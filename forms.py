"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()]
        )
    species = SelectField("Species",
                          choices =[("cat", "Cat"),
                                    ("dog", "Dog"),
                                    ("porcupine", "Porcupine")])
    photo_url = StringField("Image URL", validators=[URL(), Optional()])
    age = SelectField("Age",
                      choices = [("baby", "Baby"),
                                 ("young", "Young"),
                                 ("adult", "Adult"),
                                 ("senior", "Senior")])
    notes = StringField("Additional Information", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = photo_url = StringField("Image URL", validators=[URL(), Optional()])

    notes = StringField("Additional Information", validators=[Optional()])

    available = BooleanField("Is Available?")