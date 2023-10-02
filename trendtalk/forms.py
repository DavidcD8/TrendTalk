from django import forms
from .models import Profile, Comment
from .models import Profile
from django.contrib.auth.models import User

# Form for editing user details in the admin panel


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    profile_photo = forms.ImageField(label='Profile Photo', required=False)

# Form for editing the user profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']

# Form for adding comments to posts


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
