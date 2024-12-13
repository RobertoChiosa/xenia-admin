from django import forms
from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = [
            "name",
            "surname",
            "birth_date",
            "birth_place",
            "citizenship",
            "fiscal_code",
            "residence_address",
            "id_card_front",
            "id_card_back",
            "email",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "surname": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "birth_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "birth_place": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "citizenship": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "fiscal_code": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "residence_address": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "id_card_front": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "id_card_back": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "type": "email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'form-control' to all fields if not explicitly set
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get("class"):
                field.widget.attrs["class"] = "form-control"
