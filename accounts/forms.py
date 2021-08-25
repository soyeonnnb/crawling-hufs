from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailField
from .validators import RegisteredEmailValidator


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'nickname')
    def clean_email(self):
        original_email = self.cleaned_data.get('email')
        email_username = original_email.split('@')[0] 
        email_domain = original_email.split('@')[1]
        if email_domain != 'hufs.ac.kr':
            raise forms.ValidationError('학교 이메일만 인증이 가능합니다. example@hufs.ac.kr') 
        return email_username + '@hufs.ac.kr'
class LoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

class VerificationEmailForm(forms.Form):
    email = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), validators=(EmailField.default_validators + [RegisteredEmailValidator()]))
