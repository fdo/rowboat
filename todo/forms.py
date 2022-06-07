from django import forms

#LOOK AT https://www.techwithtim.net/tutorials/django/simple-forms/

class RunningForm(forms.Form):
    data = forms.CharField(label="How did it go?", max_length=200)
    minutes = forms.IntegerField(label="Time")

class AddWeightForm(forms.Form):
    data = forms.CharField(label="Comments", max_length=200)
    damage = forms.DecimalField(label="Weight",max_digits=4, decimal_places=1)

class RepsForm(forms.Form):
    exercise = forms.CharField(max_length=60)
    reps = forms.IntegerField()
    more = forms.CharField(max_length=200)

class CreateForm(forms.Form):
    data = forms.CharField(max_length=200)
    damage = forms.DecimalField(max_digits=4, decimal_places=1)
