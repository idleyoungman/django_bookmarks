from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(label=u'Username', max_length=30)
	email = forms.EmailField(label=u'Email')
	password1 = forms.CharField(
		label = u'Password',
		widget = forms.PasswordInput()
	)
	password2 = forms.CharField(
		label = u'Password (Again)',
		widget = forms.PasswordInput()
	)
