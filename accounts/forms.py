from allauth.account.forms import SignupForm
from django import forms
from .models import Prefecture, User

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=255, label='名前', required=True)
    furigana = forms.CharField(max_length=255, label='フリガナ', required=True)
    prefecture = forms.ModelChoiceField(queryset=Prefecture.objects.all(), label='都道府県', required=True)
    address = forms.CharField(widget=forms.Textarea, label='住所', required=True)
    phone_number = forms.CharField(max_length=20, label='電話番号', required=True)

    def save(self, request):
        user = super().save(request)
        user.name = self.cleaned_data['name']
        user.furigana = self.cleaned_data['furigana']
        user.prefecture = self.cleaned_data['prefecture']
        user.address = self.cleaned_data['address']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user