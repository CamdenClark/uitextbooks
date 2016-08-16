from django import forms
import datetime

class SearchForm(forms.Form):
	subject_code = forms.CharField(label='Subject Code (eg AMST or MATH)', min_length=1, max_length=4)
	class_number = forms.CharField(label='Class Number (eg 101 or 222)', min_length=2, max_length=4)

class SubmitForm(forms.Form):
	title = forms.CharField(label = 'Title of Book/Listing', min_length=3, max_length=200)
	email = forms.CharField(label='Email', min_length=5, max_length=100)
	price = forms.CharField(max_length=20)
	body = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':20}),max_length=1500)
	subject = forms.CharField(max_length=4)
	course_number = forms.CharField(max_length=4)
	password = forms.CharField(max_length=20, min_length=4)
