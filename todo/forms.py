from django.contrib.auth.forms import User, UserCreationForm
from django.forms import ModelForm
from .models import TodoItem


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]


class UpdateTodoItem(ModelForm):
    class Meta:
        model = TodoItem
        # fields = ["title", "status"]
        fields = ["title", "status"]
