from django import forms
import datetime

GENDER_CHOICES = [('male', '男'), ('female', '女')]
BIRTH_YEAR_CHOICES = [i for i in range(1900, datetime.datetime.now().year+1)]
class LoginForm(forms.Form):
    user_id = forms.CharField(max_length =30)
    password = forms.CharField(max_length = 30)

class RegisterForm(forms.Form):
    name = forms.CharField(max_length =30) # 姓名
    #birth = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)) # 出生年月日
    gender = forms.ChoiceField(choices = GENDER_CHOICES) # 生理性別
