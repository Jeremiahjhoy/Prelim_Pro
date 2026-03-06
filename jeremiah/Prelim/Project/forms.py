from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# ================================
# LOGIN FORM
# ================================

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'input-field'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'input-field'
        })
    )


# ================================
# ADD ADMIN FORM
# ================================

class AddAdminForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'input-field'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        user.is_staff = True
        user.is_superuser = True

        if commit:
            user.save()

        return user