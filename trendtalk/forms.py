from django import forms
from .models import Profile, Comment


class ProfilePhotoForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")

    class Meta:
        model = Profile
        fields = ('profile_image', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
