from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models
ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)
SINGLE = 1
MARRIED = 2
DIVORCED = 3

MARITAL_STATUS = (
    (SINGLE, "SINGLE"),
    (MARRIED, "MARRIED"),
    (DIVORCED, "DIVORCED")
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

#class LoginForm(AuthenticationForm):
#    def __init__(self, *args, **kwargs):
#        super(LoginForm, self).__init__(*args, **kwargs)
#
#        username = UsernameField(widget=forms.TextInput(attrs={
#            'class': 'form-control',
#            'placeholder': 'ваш логин',
#            'id': 'hello'
#        }))
#
#        password = forms.CharField(
#            widget=forms.PasswordInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'pass',
#                    'id': 'hi'
#                }
#            )
#        )