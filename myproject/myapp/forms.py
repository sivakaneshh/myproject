from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['phone_number']  # Store phone_number in email field
        user.phone_number = self.cleaned_data['phone_number']  # Store phone_number separately
        
        if commit:
            user.save()

        return user

