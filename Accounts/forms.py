from django import forms
from .models import Account



class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder':"Enter Password",
        'class':'form-control',
    }))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder':"Enter Password",
        'class':'form-control',
    }))


    class Meta:
        model = Account
        fields = ['first_name','last_name','email','phone_number','password']


    def __init__(self, *args, ** kwargs):

        super(RegistrationForm,self).__init__( *args, ** kwargs)
        self.fields['first_name'].widget.attrs['Placeholder'] = 'Enter first_name'
        self.fields['last_name'].widget.attrs['Placeholder'] = 'Enter last_name'
        self.fields['email'].widget.attrs['Placeholder'] = 'Enter email'
        self.fields['phone_number'].widget.attrs['Placeholder'] = 'Enter phonenumber'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
