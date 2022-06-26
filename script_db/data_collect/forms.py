from django import forms


class TelegramIDForm(forms.Form):
    telegram_id = forms.IntegerField(help_text='@')
