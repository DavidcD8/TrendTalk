from django import forms
from .models import Profile, Comment
from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
