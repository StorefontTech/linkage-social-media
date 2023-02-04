from django import forms

from users.models import User


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={"class": "form-control active", "required": True, "placeholder": "John", }),
            'last_name': forms.TextInput(
                attrs={"class": "form-control", "required": True, "placeholder": "Doe"}),
            'username': forms.TextInput(
                attrs={"class": "form-control", "required": True, "placeholder": "JohnDoe54"}),
            'email': forms.EmailInput(
                attrs={"class": "form-control", "required": True, "placeholder": "example@gmail.com",
                       }),
            'password': forms.PasswordInput(
                attrs={"class": "form-control", "required": True, "placeholder": "******"}),
        }
        help_texts = {
            "username": ""
        }
