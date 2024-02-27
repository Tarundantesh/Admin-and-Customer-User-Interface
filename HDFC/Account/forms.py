from django import forms
from Account.models import AccountHolder
class AccountForm(forms.ModelForm):
    class Meta:
        model=AccountHolder
        fields='__all__'
