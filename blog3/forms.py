from django import forms
class Login_form(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput,max_length=100)



class Signup_form(forms.Form):
	username = forms.CharField(label='username',max_length=100)
	password = forms.CharField(widget=forms.PasswordInput,max_length=100)
	email = forms.EmailField(max_length=100)
	firstname = forms.CharField(max_length=100)
	lastname = forms.CharField(max_length=100)
	city = forms.CharField(max_length=100)
	


class forgot_password_form(forms.Form):
	email = forms.EmailField(max_length=100)


class password_change_form(forms.Form):
	# username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput,max_length=100)
	# email = forms.EmailField(max_length=100)