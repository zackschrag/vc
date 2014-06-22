from django import forms
from django.contrib.auth.models import User
from vc_auth.models import Chapter

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError("Passwords do not match")

		return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

class ChapterForm(forms.ModelForm):
	chapter_name = forms.CharField(widget=forms.TextInput())

	class Meta:
		model = Chapter
		fields = ('chapter_name',)