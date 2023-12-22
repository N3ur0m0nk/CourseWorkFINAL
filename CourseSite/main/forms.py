from django import forms
import datetime


class Dogovor(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)
	FullFIO = forms.CharField(label="FullFIO ", max_length=300)
	Specialty = forms.CharField(label="Specialty", max_length=300)
	FullKafedra = forms.CharField(label="FullKafedra", max_length=300)
	Kafedra = forms.CharField(label="Kafedra", max_length=300)
	Birthday = forms.DateField(initial=datetime.date.today)
	Passport_Number = forms.CharField(label="Pass_Num", max_length=300)
	Passport_Vidacha = forms.CharField(label="Pass_Vidacha", max_length=300)
	Passport_Date = forms.DateField(initial=datetime.date.today)
	Registration_Address = forms.CharField(label="Reg_Address", max_length=300)