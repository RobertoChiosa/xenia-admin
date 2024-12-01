#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from django import forms


class AvailabilityForm(forms.Form):
    arrival_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    departure_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control", "label": None}
        ),
    )
    guests = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "N. Guests",
            }
        ),
    )
