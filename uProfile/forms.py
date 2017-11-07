from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model =  User
        fields = ['username','email','password']

class Qtn(forms.Form):
    # CHOICES = (('1', 'First',), ('2', 'Second',))

    heading = forms.CharField(max_length= 200)
    questions = forms.CharField(
        max_length=3000,widget=forms.Textarea(),
        help_text="Write full question",
    )
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)


    CHOICES = (('select1',option1),('select2',option2),('select2',option3),('select2',option4))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)






