from django import forms

class KeyInputForm(forms.Form):
    public_key = forms.CharField(required=True, label='Ссылка на ресурс')